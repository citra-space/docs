---
title: Hardware Adapters
nav_order: 2
parent: CitraScope
has_children: true
---

# Hardware Adapters

CitraScope uses hardware adapters to communicate with your telescope equipment. You choose an adapter based on your hardware and platform.

## Choosing an Adapter

Most operators will use one of the two primary adapters:

- **Direct Hardware** — CitraScope controls your devices end-to-end with no intermediary software. This is the recommended path for Linux, macOS, and Raspberry Pi deployments. Supports ZWO ASI cameras, Moravian cameras, ZWO AM3/AM5/AM7 mounts, ZWO EAF focusers, and more.
- **N.I.N.A.** — For Windows setups running N.I.N.A. with Planewave mounts. CitraScope communicates with N.I.N.A.'s Advanced API to control your entire equipment chain.

Additional adapters are available for specific environments:

- **KStars** — For operators already using KStars/Ekos on Linux or macOS. Communicates via D-Bus.
- **INDI** — Basic mount and camera control via the INDI protocol on Linux. Best for simple setups or custom INDI configurations.

## Capability Comparison

Not every adapter supports every feature. This table shows what each adapter can do:

| Capability | Direct Hardware | N.I.N.A. | KStars | INDI |
|---|:---:|:---:|:---:|:---:|
| **Mount control** (slew, track) | ✅ | ✅ | ✅ | ✅ |
| **Camera control** (exposure, capture) | ✅ | ✅ | ✅ | ✅ |
| **Filter wheel** | ✅ | ✅ | ✅ | — |
| **Filter renaming** | ✅ | — | — | — |
| **Focuser control** | ✅ | ✅ | — | — |
| **Autofocus** | ✅ | ✅ | — | — |
| **Custom tracking rates** | ✅ | — | — | ✅ |
| **Plate solving** | ✅ | ✅ | ✅ | — |
| **Alignment / pointing model** | ✅ | — | — | — |
| **Park / unpark** | — | ✅ | — | — |
| **Camera preview / live view** | ✅ | ✅ | — | — |
| **Safety monitor** | — | ✅ | — | — |
| **Calibration frame capture** | ✅ | ✅ | — | — |
| **Platform** | Linux, macOS, Pi | Windows | Linux, macOS | Linux |

{: .note }
> Direct Hardware capabilities depend on which devices you connect. For example, autofocus requires both a camera and a focuser. Filter wheel support requires a compatible filter wheel device.

## How Adapters Work

When you select an adapter in the Configuration tab, CitraScope loads that adapter and presents its settings. Each adapter defines its own connection parameters (e.g., an API URL for N.I.N.A., a D-Bus service name for KStars, or device selections for Direct Hardware).

Once connected, the adapter translates CitraScope's task commands into the appropriate protocol for your hardware. The rest of the system — task polling, processing pipeline, upload — works identically regardless of which adapter you choose.
