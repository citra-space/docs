---
title: Image Uploads
nav_order: 2
parent: Telescopes
grand_parent: Sensors
---

# Image Uploads

The Image Uploads section on the telescope detail page displays all observation images captured by this telescope. As a telescope owner, this is where you manage your uploaded imagery and review processing results.

## Understanding Image Uploads

Image uploads are FITS files containing telescope observations that have been submitted for processing. The platform performs automated analysis to identify satellites and other objects in the captured frames. This telescope-level view shows images from this specific instrument, whereas the [satellite-level image uploads page](../../satellites/details/image-uploads.md) shows images aggregated from all telescopes that have observed a given satellite.

## Image Uploads Grid

The images are displayed in a searchable grid:

| Column | Description |
|--------|-------------|
| **Filename** | Name of the uploaded FITS file |
| **Status** | Current processing status |
| **Created** | Timestamp when the image was uploaded |
| **Username** | User who uploaded the image |
| **Original** | Button to view the original unprocessed image |
| **Processed** | Button to view the processed image with detected objects |
| **Downloads** | Download the FITS file or object catalog |
| **Delete** | Remove the image (owner only) |

## Processing Status

Uploaded images progress through the following statuses:

| Status | Description |
|--------|-------------|
| **Pending** | Image is queued and waiting to be processed |
| **Uploading** | Image file is being transferred to the platform |
| **Processing** | Automated analysis is underway |
| **Completed** | Processing finished successfully with results available |
| **Failed** | Processing encountered an error |

## FITS Viewer

Select a view button to open the FITS viewer, which provides:

- **Image tab** — Displays the observation image with ZScale contrast adjustment for optimal visibility
- **Headers tab** — Shows FITS header metadata including observation parameters, timestamps, and equipment details
- **Zoom and pan** — Interactive controls to zoom in, pan across, and reset the image view

## Downloading Data

For completed images, two download options are available:

- **FITS file** — The processed astronomical image in FITS format
- **Object catalog** — A catalog of detected objects with positions and identifications

## Deleting Images

Select the delete button to remove an image upload. A confirmation dialog will appear before the image is permanently deleted.

{: .important }
> Only the telescope owner can delete image uploads.

## Use Cases

Telescope image uploads support:

- **Observation review** — Examining captured images to verify satellite detections
- **Data quality assessment** — Checking processing results and FITS headers for accuracy
- **Data management** — Organizing and maintaining the telescope's observation archive
