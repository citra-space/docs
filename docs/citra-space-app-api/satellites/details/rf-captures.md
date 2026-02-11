---
title: RF Captures
nav_order: 3
parent: Details and Tools
grand_parent: Satellites
---

# RF Captures

The RF Captures section on the Observations tab displays radio frequency capture data collected from tasks associated with the satellite.

## Understanding RF Captures

RF captures are recordings of radio signals transmitted by or reflected from a satellite. These captures are collected by ground-based antennas during scheduled observation tasks and can be used for:

- Signal analysis and characterization
- TDOA (Time Difference of Arrival) geolocation
- Frequency monitoring and verification
- Communication pattern analysis

## RF Captures List

The RF captures are displayed in a searchable grid showing all captures associated with the satellite:

| Column | Description |
|--------|-------------|
| **Capture Time** | When the RF capture was recorded |
| **Antenna** | The antenna that collected the capture |
| **Ground Station** | The ground station where the antenna is located |
| **Status** | Processing status of the capture |
| **Actions** | View or download the capture data |

## Viewing RF Captures

Select a capture from the list to view detailed information including:

- **Capture metadata** - Recording parameters and equipment details
- **Signal data** - Frequency, bandwidth, and signal characteristics
- **Processing results** - Any automated analysis that has been performed

{: .note }
> RF captures shown on the satellite detail page are aggregated from all antennas that have observed this satellite. To upload new RF captures, navigate to the specific antenna's detail page.

## Related Resources

- [Add and Manage Antennas](../../../guides-and-tutorials/add-and-manage-antennas) - Learn how to set up antennas for RF observation
- [API Documentation](https://api.citra.space/docs#/rf_captures) - Programmatic access to RF capture data
