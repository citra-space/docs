# Citra Space Documentation

Welcome to Citra Space! Here you'll find all the information you need to get started with Citra Space, including app walkthroughs, hardware setup, and support.

## Quick Links

Visit the app:
https://app.citra.space

API Documentation:
https://api.citra.space/docs

Discord:
https://discord.gg/STgJQkWe9y

Get News Updates:
(CRM link soon)

## Contents

- [Citra Space Overview](#citra-space-overview)
- [Support](#support)
- [Getting Started](#getting-started)
- [App Walkthroughs](#app-walkthroughs)
  - [Sign Up & Authentication](#sign-up--authentication)
  - [Dashboard/Home Page](#dashboardhome-page)
  - [Satellites](#satellites)
  - [Ground Stations](#ground-stations)
  - [Sensors](#sensors)
  - [Observations](#observations)
  - [Access Windows](#access-windows)
  - [User Profile & Settings](#user-profile--settings)
- [API Documentation](#api-documentation)
- [Hardware Setup](#hardware-setup)
- [FAQs](#faqs)
- [Contribute](#contribute)

## Citra Space Overview

### _Our Mission:_

_Citra provides modular sensing and software solutions for detecting, tracking, and identifying orbiting objects to ensure safe and sustainable space operations for all._

The Citra Space platform currently offers:
- Optical and RF contributions and observation tools for amateur and enterprise users alike
- Satellite observation scheduling
- Satellite access window calculation
- Satellite residuals analysis
- Observation data collection and access
- Ground station management
- Telescope and antenna management
- Observation data processing and analysis
- Integration with UDL, Space Track, SatNOGS and you!
- API access for hardware observation submissions and analysis
- Close approach detection and analysis
- Real-time weather data for ground stations
- Group collaboration features

More solutions are on the way.

## Support

For general community and team support, please join our Discord server:
https://discord.gg/STgJQkWe9y

We can also be reached via email (see the email link in the app).

## Getting Started

(Overview of first steps - creating account, setting up first ground station, adding first sensor, etc.)

## App Walkthroughs

### Sign Up & Authentication

(soon)

- Creating an account
- Logging in with OIDC
- Managing your profile

### Dashboard/Home Page

The Citra Space dashboard provides an at-a-glance overview of the platform:

#### Satellites Overview Section
(soon)

- **Satellite Counts**: Overview of total satellites tracked in the catalog
- **Hourly Optical Observation Counts**: Chart showing optical observation activity over time
- **Element Set (Elset) Counts**: Statistics on available orbital element sets
- **LEO Scatter Plot**: Visualization of Low Earth Orbit satellites
- **Near-GEO Scatter Plot**: Visualization of Geosynchronous orbit satellites

#### Ground Stations Map
(soon)

- Interactive map showing all ground stations in the network
- Filter and search ground stations
- View ground station details from the map

#### Sensors Overview
(soon)

- Summary of telescopes and antennas in the network
- Quick access to sensor management

### Satellites

#### Browsing Satellites
(soon)

- Searching and filtering the satellite catalog
- Understanding satellite information
- Navigating to satellite detail pages

#### Satellite Detail Pages
(soon)

Satellite detail pages provide comprehensive information about each tracked object:

##### Basic Information
- Satellite ID and name
- Creation epoch
- Decay epoch (if applicable)

##### Aliases
- Multiple names and identifiers from different data providers (Space-Track, SatNOGS, UDL, etc.)
- Data source attribution

##### Transmissions
- Known RF transmission frequencies
- Transmission characteristics
- Data source information

##### RF Captures
(soon)

- Radio frequency observations from antennas
- Uploading RF observation data
- Viewing RF capture history

##### Image Uploads (Optical Observations)
(soon)

- Optical observations from telescopes
- Uploading telescope images
- Viewing observation history
- Image metadata and analysis

##### Tasking Schedule
(soon)

- Scheduling future observations
- Managing observation priorities
- Viewing scheduled tasks

##### Access Windows
(soon)

- Calculating when a satellite is visible from specific ground stations
- Understanding access window parameters
- Filtering by ground station and constraints

##### Close Approaches
(soon)

- Calculating close approaches with other satellites
- Understanding conjunction warnings
- Proximity analysis

##### Observation Residuals
(soon)

- Understanding residuals (difference between predicted and observed position)
- Radial, in-track, and cross-track error components
- Interpreting residual charts
- Identifying orbital maneuvers from residuals

##### Element Sets (Elsets)
(soon)

- Current and historical orbital element sets
- TLE (Two-Line Element) data
- Element set sources and epochs

### Ground Stations

#### Browsing Ground Stations
(soon)

- Viewing all ground stations on the map
- Searching and filtering ground stations
- Understanding ground station capabilities

#### Creating a Ground Station
(soon)

- Adding a new ground station
- Required information (name, latitude, longitude, altitude)
- Best practices for ground station setup

#### Ground Station Detail Pages
(soon)

Ground station pages provide tools for managing your observing site:

##### Location & Details
- Geographic coordinates
- Altitude
- Edit and update information

##### Access Window Calculation
(soon)

- Calculate satellite passes for your location
- Set observation constraints (minimum elevation, etc.)
- Export access windows

##### Associated Sensors
(soon)

- List of telescopes and antennas at this ground station
- Quick access to sensor details
- Adding sensors to the ground station

##### Weather Information
(soon)

- Real-time weather data for your location
- Weather forecasts
- Planning observations around weather conditions

#### Managing Ground Stations
(soon)

- Editing ground station information
- Deleting ground stations
- Transfer between ground stations

### Sensors

Sensors include both telescopes (for optical observations) and antennas (for RF observations).

#### Browsing Sensors
(soon)

- Viewing all your sensors
- Filtering by type (telescope vs. antenna)
- Understanding sensor capabilities

#### Creating Sensors

##### Adding a Telescope
(soon)

- Required information:
  - Name
  - Ground station assignment
  - Field of view
  - Maximum magnitude
  - Minimum elevation
  - Maximum slew rate
  - Home position (azimuth, elevation)
  - Angular noise
- Configuration best practices

##### Adding an Antenna
(soon)

- Required information:
  - Name
  - Ground station assignment
  - Frequency range (min/max)
  - Minimum elevation
  - Maximum slew rate
  - Home position (azimuth, elevation)
  - Half-power beam width
- Configuration best practices

#### Telescope Detail Pages
(soon)

- Telescope specifications and configuration
- Tasking schedule for the telescope
- Image uploads and observation history
- Editing telescope settings
- Deleting telescopes

#### Antenna Detail Pages
(soon)

- Antenna specifications and configuration
- Tasking schedule for the antenna
- RF capture history
- Editing antenna settings
- Deleting antennas

### Observations

#### Optical Observations (Image Uploads)
(soon)

- How to upload telescope images
- Required metadata
- Image formats and requirements
- Viewing and managing your observations
- Observation quality and validation

#### RF Observations (RF Captures)
(soon)

- How to upload RF observation data
- Required metadata
- Data formats and requirements
- Viewing and managing your RF captures
- Signal analysis

#### Observation Data Quality
(soon)

- Understanding observation residuals
- Data validation
- Quality metrics
- Best practices for high-quality observations

### Access Windows

(soon)

- What are access windows?
- Calculating satellite passes
- Access constraints:
  - Minimum elevation
  - Time windows
  - Custom constraints
- Interpreting access window results
- Exporting access window data
- Using access windows for observation planning

### User Profile & Settings

#### Profile
(soon)

- Viewing your profile information
- User details and authentication info

#### Settings
(soon)

- Browser settings and preferences
- Application configuration

#### Access Tokens
(soon)

- What are Personal Access Tokens (PATs)?
- Creating API access tokens
- Managing your tokens (maximum 5 tokens)
- Using tokens for API authentication
- Security best practices
- Revoking tokens

#### Groups
(soon)

- Understanding groups and collaboration
- Viewing your group membership
- Group member management (for group admins)
- Group-level permissions

#### Admin Features
(soon)

- Platform administration tools
- User management
- Group administration
- System monitoring

## API Documentation

The Citra Space API provides programmatic access to the platform:

### API Access
(soon)

- API endpoint: https://api.citra.space/docs
- Authentication with Personal Access Tokens
- API rate limits and quotas

### Common API Operations
(soon)

- Submitting observations
- Querying satellites
- Calculating access windows
- Retrieving orbital elements
- Managing sensors

### API Examples
(soon)

- Python examples
- JavaScript examples
- cURL examples

## Hardware Setup

### Telescope Setup
(soon)

- Hardware requirements
- Software configuration
- Integration with Citra Space API
- Automated observation workflows
- Calibration and testing

### Antenna Setup
(soon)

- Hardware requirements
- Software configuration
- Integration with Citra Space API
- Automated RF capture workflows
- Calibration and testing

### Ground Station Setup
(soon)

- Site selection
- Equipment recommendations
- Network connectivity
- Power and environmental considerations

## FAQs

### General Questions
(soon)

- What is Citra Space?
- Who can use Citra Space?
- Is Citra Space free?

### Technical Questions
(soon)

- What data sources does Citra Space use?
- How accurate are the orbital predictions?
- What observation formats are supported?
- How do I integrate my hardware?

### Observation Questions
(soon)

- What makes a good observation?
- How are observations validated?
- What happens to my observation data?
- Can I share observations with others?

### Account & Access Questions
(soon)

- How do I reset my password?
- How do I join a group?
- What are the API rate limits?
- How do I get API access?

## Contribute

### Contributing Observations
(soon)

- How your observations help
- Observation guidelines
- Data sharing and attribution

### Contributing to Development
(soon)

- Open source contributions
- Feature requests
- Bug reports

### Community Involvement
(soon)

- Join the Discord
- Participate in discussions
- Share your projects
- Collaborate with other users

### Feedback
(soon)

- How to provide feedback
- Feature suggestions
- Report issues
