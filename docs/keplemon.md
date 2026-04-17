---
title: KepLemon
nav_order: 5
---

# KepLemon
{: .no_toc }

KepLemon is a Rust-accelerated astrodynamics Python library developed by Citra Space. It provides high-performance satellite propagation, orbit determination, and close approach detection capabilities, and is used internally by the Citra Space app to power its orbital analysis features.

## Key Features

- **High-performance propagation** — Rust core with Python bindings for fast SGP4 and SGP4-XP satellite propagation
- **Orbit determination** — Tools for fitting orbital elements to observation data
- **Close approach detection** — Efficiently screen large catalogs for conjunction events
- **Easy installation** — Install with `pip install keplemon`, no Rust toolchain required
- **Multi-threaded batch propagation** — Parallel propagation of satellite constellations using Rayon
- **Built on space-track.org shared libraries** — Leverages community-standard astrodynamics routines

## Getting Started

Install KepLemon from PyPI:

```bash
pip install keplemon
```

Visit the [KepLemon documentation](https://keplemon.citra.space) for usage guides, API reference, and examples.

## Open Source and Contributing

KepLemon is open source and available on [GitHub](https://github.com/citra-space/keplemon). Contributions, bug reports, and feature requests are welcome.
