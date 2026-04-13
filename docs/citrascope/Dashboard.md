---
title: Web Dashboard
nav_order: 7
parent: CitraScope
has_children: true
---

# Web Dashboard

CitraScope includes a local web dashboard for monitoring and configuring your telescope. Once the daemon is running, open your browser to:

```
http://localhost:24872
```

On Raspberry Pi deployments, the dashboard is also available at `http://citrascope.local`.

The port number (24872) spells "CITRA" on a phone keypad.

## Sections

The dashboard has two main tabs:

- **[Monitoring](Monitoring.html)** — Live view of your telescope, camera, task pipeline, and operational controls. This is the default view when you open the dashboard.
- **Configuration** — Hardware adapter selection, API connection, observation settings, processor toggles, autofocus scheduling, and advanced options.

A collapsible **Log Panel** at the bottom of every page streams real-time log output from the daemon.

## Design

The dashboard uses a dark theme to preserve night vision during observatory use. It is responsive and works on tablets and phones in the field.

All status updates arrive over a WebSocket connection, so the dashboard reflects the current state of the system without manual refreshing. The "Daemon" badge in the status bar shows whether this live connection is active.
