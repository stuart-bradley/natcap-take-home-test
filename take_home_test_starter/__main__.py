import argparse
import os

import fiona
import rasterio
import rasterio.mask


def main() -> None:
    """
    This script performs the following tasks:
    1. Opens a Shapefile via Fiona (GDAL)
    2. Downloads related GeoTIFF Files (Boto3 or direct download).
    3. Merge related GeoTIFF files (GDAL Merge).
    4. Uses Rasterio to create a mask with only the area of interest.
      (https://rasterio.readthedocs.io/en/stable/topics/masking-by-shapefile.html)
    """

    #parser = argparse.ArgumentParser(description='Generates GeoTIFF files from Shapefiles')
    #parser.add_argument('filename')
    #parsed_args = parser.parse_args()

    with fiona.open("/app/take_home_test_starter/world-administrative-boundaries.shp", "r") as shapefile:
        shapes = [feature["geometry"] for feature in shapefile]

if __name__ == "__main__":
    main()
