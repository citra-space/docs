---
title: Browsing and Filtering
nav_order: 1
parent: Ground Stations
---

# Browsing and Filtering

The Ground Stations page displays a list of all ground stations available to you. Use this page to browse, create, and manage ground station locations.

## Quick Search

The search bar at the top of the ground station list filters stations as you type, making it easy to locate a specific site.

## Columns

The ground station list displays the following columns:

| Column | Description |
|--------|-------------|
| **Name** | Ground station name (click to navigate to the detail page) |
| **Latitude** | Geographic latitude in decimal degrees |
| **Longitude** | Geographic longitude in decimal degrees |
| **Altitude** | Elevation above sea level in meters |
| **Actions** | Edit and delete buttons (visible only to the station owner) |

## Adding a Ground Station

Select the `Add Ground Station` button in the toolbar to open the creation form in a side panel.

### Form Fields

| Field | Description |
|-------|-------------|
| **Name** | A descriptive name for the ground station (required) |
| **Latitude** | Geographic latitude in decimal degrees (-90 to 90) |
| **Longitude** | Geographic longitude in decimal degrees (-180 to 180) |
| **Altitude** | Elevation above sea level in meters (minimum 0) |

{: .note }
> Latitude and longitude use decimal degrees. For example, Washington, D.C. is approximately 38.9 latitude, -77.0 longitude.

## Editing a Ground Station

Select the edit button in the Actions column to open the same form pre-filled with the station's current values. Make your changes and save.

{: .important }
> Edit and delete actions are only available for ground stations that you own.

## Deleting a Ground Station

Select the delete button in the Actions column to remove a ground station. A confirmation dialog will appear before the station is permanently deleted.

## Pagination

Use the pagination controls at the bottom of the list to navigate between pages. Available page sizes are **10**, **25**, and **100** rows per page.

## Navigating to Details

Click a ground station name in the list to open its detail page, where you can calculate satellite passes, manage sensors, and view weather data. See the [Details and Tools](details/) section for more information.
