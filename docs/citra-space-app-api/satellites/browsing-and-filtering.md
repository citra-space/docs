---
title: Browsing and Filtering
nav_order: 1
parent: Satellites
---

# Browsing and Filtering

The Satellites page displays a searchable, filterable list of all satellites in the Citra Space catalog. Use this page to find satellites by name, identifier, or country of origin and navigate to detailed satellite profiles.

## Quick Search

The search bar at the top of the satellite list performs a debounced text search across satellite names and aliases. Start typing to filter the list in real time.

## Column Filters

Click the filter icon on any column header to apply column-specific filters. Each column supports different filter types:

| Column | Filter Type | Description |
|--------|-------------|-------------|
| **Name** | Text | Filter satellites by name using contains, equals, starts with, or ends with operators |
| **NORAD ID** | Numeric | Filter by NORAD catalog number using numeric comparison operators |
| **Country** | Select | Filter by country of origin using is, is not, or is any of operators. Country options display with flag icons for quick identification |
| **Decay Epoch** | Date | Filter by decay date to find satellites that decayed within a specific time range |

## Display Columns

The satellite list includes several informational columns:

| Column | Description |
|--------|-------------|
| **Name** | Satellite name (click to navigate to the detail page) |
| **NORAD ID** | U.S. Space Command catalog number |
| **Country** | Country of origin with flag icon |
| **Aliases** | Number of known alternative names and identifiers |
| **Element Sets** | Number of orbital element sets available |
| **Transmissions** | Number of known radio frequency transmissions |
| **Decay Epoch** | Date the satellite decayed, if applicable |

## Show Decayed Toggle

By default, the satellite list excludes satellites that have re-entered the atmosphere. Enable the **Show Decayed** checkbox in the toolbar to include decayed satellites in the list. This is useful for historical research or verifying decay dates.

## Sorting

Click a column header to sort the list by that column. Click again to toggle between ascending and descending order.

## Pagination

The satellite list uses server-side pagination. Use the pagination controls at the bottom of the list to navigate between pages. Available page sizes are **10**, **25**, **50**, and **100** rows per page.

## Actions

The toolbar includes a satellite group management button for organizing satellites into custom groups.

## URL Persistence

All filter, sort, and pagination settings are persisted in the browser URL. This means you can:

- **Bookmark** a filtered view to return to it later
- **Share** a specific filtered view with colleagues by copying the URL
- **Use browser navigation** to move back and forth between filter states

## Navigating to Details

Click a satellite name in the list to open its detail page, where you can view aliases, transmissions, orbital elements, and analysis tools. See the [Details and Tools](details/) section for more information.
