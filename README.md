# Atlas-magnetic

**Atlas-magnetic** is an interactive web atlas of the Earth's magnetic field based on the International Geomagnetic Reference Field (IGRF).

The project provides a lightweight 3D globe that visualizes global magnetic field data from **1900 to 2025**. Two datasets are included:

* **Magnetic field intensity (F)**
* **Magnetic declination (D)**

## Repository contents

* `index.html` – interactive web viewer built with Three.js
* `atlas_intensity.webp` – texture atlas containing magnetic field intensity maps
* `atlas_declination.webp` – texture atlas containing magnetic declination maps
* `metadata.json` – atlas metadata and frame information
* `render_atlas.py` – Python script used to generate the atlas from IGRF data

## Data source

The atlas is generated using the **International Geomagnetic Reference Field (IGRF)** through the Python `ppigrf` package.

## Features

* Interactive 3D globe
* Global magnetic field visualization
* Time coverage: **1900–2025**
* Texture-atlas rendering for efficient web display

## License

This repository is intended for research, educational, and visualization purposes.
