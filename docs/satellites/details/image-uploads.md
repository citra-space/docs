---
title: Image Uploads
nav_order: 4
parent: Details and Tools
grand_parent: Satellites
---

# Image Uploads

The Image Uploads section on the Observations tab displays optical observation images associated with the satellite.

## Understanding Image Uploads

Image uploads are telescope observations that have been processed to identify and track satellites. These images are collected by ground-based telescopes during scheduled observation tasks and provide visual confirmation of satellite position and characteristics.

## Image Uploads List

The images are displayed in a searchable grid showing all uploads associated with the satellite:

| Column | Description |
|--------|-------------|
| **Upload Time** | When the image was uploaded |
| **Telescope** | The telescope that captured the image |
| **Ground Station** | The ground station where the telescope is located |
| **Status** | Processing status (Queued, Processing, Completed, Failed) |
| **Actions** | View, download FITS file, or download object catalog |

## Processing Status

Uploaded images go through automated processing:

1. **Queued** - Image is waiting to be processed
2. **Processing** - Automated analysis is underway
3. **Completed** - Processing finished successfully
4. **Failed** - Processing encountered an error

## Viewing Processed Images

For completed images, select `VIEW` to open the FITS viewer which displays:

- **Image preview** - The processed observation image
- **Detected objects** - Stars and satellites identified in the frame
- **Overlay markers** - Visual indicators for detected objects
- **Image metadata** - Observation parameters and timestamps

## Downloading Data

For completed images, you can download:

- **FITS file** - The processed astronomical image in FITS format
- **Object catalog** - A catalog of detected objects with positions and identifications

{: .note }
> Images shown on the satellite detail page are aggregated from all telescopes that have observed this satellite. To upload new images, navigate to the specific telescope's detail page.

## Related Resources

- [Add and Manage Telescopes](../../guides-and-tutorials/add-and-manage-telescopes.md) - Learn how to set up telescopes for optical observation
- [API Documentation](https://api.citra.space/docs#/images) - Programmatic access to image upload functionality
