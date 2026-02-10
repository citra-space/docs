---
title: Collection Requests
nav_order: 5
parent: Details and Tools
grand_parent: Satellites
---

# Collection Requests

The Collection Requests section on the Tasking tab allows you to request and manage observation windows for the satellite.

## Understanding Collection Requests

A collection request defines a time window during which you want to observe a satellite. Once submitted, the system schedules specific observation tasks on available sensors (telescopes or antennas) that can observe the satellite during the requested window.

## Creating a Collection Request

To create a new collection request:

1. Navigate to the satellite's Tasking tab
2. Select the `REQUEST COLLECTION` button in the upper right
3. Complete the collection request form in the side panel

### Collection Request Form

| Field | Description |
|-------|-------------|
| **Collection Type** | The type of observation: Optical (telescope) or TDOA (RF geolocation) |
| **Window Start** | The beginning of the observation window (UTC) |
| **Window Stop** | The end of the observation window (UTC) |
| **Priority** | Observation priority (1-10, where 1 is highest priority) |

For TDOA collection requests, additional parameters are available:

| Field | Description |
|-------|-------------|
| **Number of Sensors** | Minimum number of antennas required for the observation |
| **Minimum Frequency (Hz)** | Lower bound of the frequency range to observe |
| **Maximum Frequency (Hz)** | Upper bound of the frequency range to observe |

Select `CREATE` to submit the collection request.

## Viewing Collection Requests

Collection requests are displayed in two tabs:

### Upcoming Tab

Shows collection requests with window end times in the future. Sorted by window start time (earliest first).

### Historical Tab

Shows collection requests with window end times in the past. Sorted by window start time (most recent first).

## Collection Requests Grid

| Column | Description |
|--------|-------------|
| **Tasks** | Number of tasks generated from this request (expandable) |
| **Window Start** | When the observation window begins |
| **Window Stop** | When the observation window ends |
| **Type** | Collection type (Optical or TDOA) |
| **Priority** | Request priority level |
| **Status** | Current status of the request |
| **Requested By** | User who created the request |

## Viewing Tasks

Select the expand arrow on any collection request row to view the tasks generated for that request. Each task represents a specific scheduled observation on a sensor.

The tasks subtable displays:

| Column | Description |
|--------|-------------|
| **Task Start** | When the task begins |
| **Task Stop** | When the task ends |
| **Status** | Task status (Pending, Scheduled, Succeeded, Failed, Canceled) |
| **Filter** | Optical filter assigned to the task (for telescope observations) |
| **Ground Station** | The ground station assigned to the task |
| **Sensor** | The specific telescope or antenna assigned |

{: .note }
> Collection requests cannot be created for decayed satellites. If a satellite has decayed, the Request Collection button will not be available.
