import io
import json
import os
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from PIL import Image
from ppigrf import igrf

YEARS = list(range(1900, 2026, 5))
COLS, ROWS = 6, 5
TILE_W, TILE_H = 1024, 512
DPI = 100
FIG_W, FIG_H = TILE_W / DPI, TILE_H / DPI

LON = np.arange(-180, 181, 3)
LAT = np.arange(-89, 90, 3)
LON2, LAT2 = np.meshgrid(LON, LAT)

OUT_DIR = "output"
os.makedirs(OUT_DIR, exist_ok=True)

def render_tile(year: int, kind: str) -> Image.Image:
    fig = plt.figure(figsize=(FIG_W, FIG_H), dpi=DPI)
    fig.patch.set_facecolor("white")
    ax = fig.add_axes([0, 0, 1, 1], projection=ccrs.PlateCarree())
    ax.set_global()
    ax.axis("off")

    Be, Bn, Bu = igrf(LON2, LAT2, 0, datetime(year, 7, 1))
    Be = np.squeeze(Be)
    Bn = np.squeeze(Bn)
    Bu = np.squeeze(Bu)

    if kind == "intensity":
        z = np.sqrt(Be**2 + Bn**2 + Bu**2)
        cmap, vmin, vmax = "inferno", 22000, 68000
    elif kind == "declination":
        z = np.degrees(np.arctan2(Be, Bn))
        cmap, vmin, vmax = "twilight", -30, 30
    else:
        raise ValueError(f"Unknown kind: {kind}")

    ax.contourf(
        LON, LAT, z,
        levels=40,
        cmap=cmap,
        transform=ccrs.PlateCarree(),
        vmin=vmin,
        vmax=vmax,
    )
    ax.add_feature(cfeature.COASTLINE, linewidth=0.4, edgecolor="black")
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=DPI, facecolor="white")
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf).convert("RGB")


def compose_atlas(kind: str) -> str:
    atlas = Image.new("RGB", (TILE_W * COLS, TILE_H * ROWS), (255, 255, 255))
    for idx, year in enumerate(YEARS):
        tile = render_tile(year, kind)
        if tile.size != (TILE_W, TILE_H):
            tile = tile.resize((TILE_W, TILE_H), Image.Resampling.LANCZOS)
        r, c = divmod(idx, COLS)
        atlas.paste(tile, (c * TILE_W, r * TILE_H))
        print(f"{kind}: {year}")
    out_path = os.path.join(OUT_DIR, f"atlas_{kind}.webp")
    atlas.save(out_path, "WEBP", quality=88, method=6)
    return out_path


def write_metadata():
    metadata = {
        "tileWidth": TILE_W,
        "tileHeight": TILE_H,
        "columns": COLS,
        "rows": ROWS,
        "years": YEARS,
        "layers": ["intensity", "declination"],
    }
    with open(os.path.join(OUT_DIR, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)


def main():
    for kind in ("intensity", "declination"):
        compose_atlas(kind)
    write_metadata()
    print("Done.")
    print(f"Files written to: {os.path.abspath(OUT_DIR)}")


if __name__ == "__main__":
    main()
