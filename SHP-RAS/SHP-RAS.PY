# Import system modules
import arcpy
from arcpy import env


def shp2raster(year):
    # Set environment settings
    env.workspace = "F:/NEW(1)/Feature"
    indicators = ["IJI", "PAFRAC", "DIVISION", "CONTAG", "SHEI", "SHDI"]
    # Set local variables
    inFeature = year + ".shp"
    for indicator in indicators:
        outRaster = "F:/NEW(1)/GRID/" + indicator + "/" + year + ".tif"
        cellSize = 3000
        field = indicator

        # Execute FeatureToRaster
        arcpy.FeatureToRaster_conversion(inFeature, field, outRaster, cellSize)


if __name__ == '__main__':
    years = ["2002", "2002s"]
    for year in years:
        shp2raster(year)
