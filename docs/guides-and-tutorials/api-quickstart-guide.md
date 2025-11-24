---
title: API Quickstart Guide
nav_order: 1
parent: Guides and Tutorials
---

# API Quickstart Guide

Welcome to the Citra Space API Quickstart Guide! This guide will help you get started with using the Citra Space API to interact with our platform programmatically. Whether you're an enthusiast wanting to automate satellite observation tasks or a developer looking to integrate Citra Space into your enterprise applications, this guide will provide you with the essential steps to get up and running.

## API Documentation

The Citra Space REST API is updated frequently. See full endpoint documentation at [https://api.citra.space/docs](https://api.citra.space/docs).

## Why Use the Citra Space API?

The Citra Space API allows you to:
- Automate satellite observation scheduling and data retrieval
- Programmatically upload telescope images and RF captures from your ground stations for analysis
- Calculate satellite access windows for optimal observation planning
- Integrate Citra Space data into your own applications and workflows
- Manage ground stations, telescopes, and antennas at scale
- Process and analyze satellite tracking data, including orbital residuals and close approach calculations
- Access real-time weather data for your observation sites

## Getting Started

To gain access to the Citra Space API, you'll first need to [create an account](../user/sign-up.md).

Then, create a personal access token by [following the instructions here](../user/access-tokens.md). Once the token is created, you can use it to make authenticated requests to the API.

## Making Your First API Request

Let's start with a simple request to verify your API access by retrieving your account information. All API requests require authentication using your personal access token in the `Authorization` header as a Bearer token.

### cURL Example

```bash
curl -X GET "https://api.citra.space/my/account" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Python Example

```python
import requests

url = "https://api.citra.space/my/account"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}

response = requests.get(url, headers=headers)
print(response.json())
```

### JavaScript Example

```javascript
const url = "https://api.citra.space/my/account";

fetch(url, {
  method: "GET",
  headers: {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
  }
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

Replace `YOUR_ACCESS_TOKEN` with the personal access token you created in the previous step. A successful response will return your account details in JSON format.

## Uploading Telescope Observations

One of the most powerful features of the Citra Space API is the ability to programmatically upload telescope images for automatic processing. The platform will detect stars and satellites in your images, generate catalogs, and provide visual overlays.

{: .note }
> Before uploading images, you'll need your telescope ID. You can find this on your telescope's detail page in the Citra Space app. If you haven't created a telescope yet, see the [Add and Manage Telescopes](./add-and-manage-telescopes.md) guide.

Uploading an image is a two-step process:
1. Initiate the upload to receive a presigned upload URL
2. Upload your FITS file to the provided URL

### Step 1: Initiate the Upload

First, call the `/my/images` endpoint with your image metadata:

#### cURL Example

```bash
curl -X POST "https://api.citra.space/my/images" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "filename": "observation_2024-01-15.fits",
    "telescope_id": "YOUR_TELESCOPE_ID",
    "file_size": 2048576,
    "max_sources": 50
  }'
```

#### Python Example

```python
import requests
import os

# Path to your FITS file
fits_file_path = "observation_2024-01-15.fits"
file_size = os.path.getsize(fits_file_path)

# Step 1: Initiate upload
url = "https://api.citra.space/my/images"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "filename": os.path.basename(fits_file_path),
    "telescope_id": "YOUR_TELESCOPE_ID",
    "file_size": file_size,
    "max_sources": 50
}

response = requests.post(url, headers=headers, json=payload)
upload_data = response.json()
print(f"Upload ID: {upload_data['upload_id']}")
```

#### JavaScript Example

```javascript
// Step 1: Initiate upload
const initiateUpload = async (file, telescopeId) => {
  const url = "https://api.citra.space/my/images";

  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Authorization": "Bearer YOUR_ACCESS_TOKEN",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      filename: file.name,
      telescope_id: telescopeId,
      file_size: file.size,
      max_sources: 50
    })
  });

  return await response.json();
};
```

### Step 2: Upload the FITS File

The response from Step 1 will include a presigned URL. Use this URL to upload your FITS file:

#### Python Example (Complete Flow)

```python
import requests
import os

fits_file_path = "observation_2024-01-15.fits"
file_size = os.path.getsize(fits_file_path)

# Step 1: Initiate upload
initiate_url = "https://api.citra.space/my/images"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "filename": os.path.basename(fits_file_path),
    "telescope_id": "YOUR_TELESCOPE_ID",
    "file_size": file_size,
    "max_sources": 50
}

response = requests.post(initiate_url, headers=headers, json=payload)
upload_data = response.json()

# Step 2: Upload the file to the presigned URL
with open(fits_file_path, 'rb') as f:
    upload_response = requests.put(
        upload_data['upload_url'],
        data=f,
        headers={'Content-Type': 'application/fits'}
    )

if upload_response.status_code == 200:
    print(f"Upload successful! Upload ID: {upload_data['upload_id']}")
    print("Your image is now being processed.")
else:
    print(f"Upload failed: {upload_response.status_code}")
```

#### JavaScript Example (Complete Flow)

```javascript
const uploadFitsFile = async (file, telescopeId) => {
  // Step 1: Initiate upload
  const initiateResponse = await fetch("https://api.citra.space/my/images", {
    method: "POST",
    headers: {
      "Authorization": "Bearer YOUR_ACCESS_TOKEN",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      filename: file.name,
      telescope_id: telescopeId,
      file_size: file.size,
      max_sources: 50
    })
  });

  const uploadData = await initiateResponse.json();

  // Step 2: Upload file to presigned URL
  const uploadResponse = await fetch(uploadData.upload_url, {
    method: "PUT",
    body: file,
    headers: {
      "Content-Type": "application/fits"
    }
  });

  if (uploadResponse.ok) {
    console.log(`Upload successful! Upload ID: ${uploadData.upload_id}`);
    console.log("Your image is now being processed.");
  } else {
    console.error(`Upload failed: ${uploadResponse.status}`);
  }
};

// Usage with file input
// const fileInput = document.querySelector('input[type="file"]');
// const file = fileInput.files[0];
// uploadFitsFile(file, "YOUR_TELESCOPE_ID");
```

### Checking Upload Status

After uploading, you can check the processing status of your image:

```bash
curl -X GET "https://api.citra.space/my/images/UPLOAD_ID" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

The image will go through several states: `PENDING` → `UPLOADED` → `PROCESSING` → `COMPLETED`. Once completed, you can view the processed image and download the catalog through the Citra Space app or via the API.

## That's Just the Start!

The Citra Space API offers a wide range of endpoints to manage ground stations, antennas, telescopes, and more. Explore the [API documentation](https://api.citra.space/docs) to discover all the capabilities available to you.

## Support

Have questions or need assistance? Join our [Discord community](https://discord.gg/STgJQkWe9y) to get support from multiple folks in the space. You can also select `Send Feedback` in the left navigation menu from within the app.
