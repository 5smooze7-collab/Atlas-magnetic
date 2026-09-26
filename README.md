# Atlas-magnetic

Atlas-magnetic is an interactive 3D web atlas of the Earth's magnetic field based on IGRF data.

It visualizes two layers:

* **Intensity (F)**
* **Declination (D)**

The atlas covers the years **1900–2025** in 5-year steps and is displayed on a rotating globe in the browser.

## Files

* `index.html` – interactive web viewer
* `metadata.json` – atlas structure and file metadata
* `field_data.json` – precomputed magnetic field values for click sampling
* `atlas_intensity.webp` – texture atlas for magnetic intensity
* `atlas_declination.webp` – texture atlas for magnetic declination
* `render_atlas.py` – Python generator script

## Features

* 3D globe view
* Mouse/touch rotation and zoom
* Time slider from 1900 to 2025
* Play/Pause animation
* Click a point on the globe to read approximate field values

## Data source

The atlas is generated from the **International Geomagnetic Reference Field (IGRF)** using the Python package `ppigrf`.

## Purpose

This project is intended for visualization, exploration, and educational use.

## License

Add your preferred license here.
