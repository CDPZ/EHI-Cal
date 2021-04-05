# Import system modules
import arcpy
from arcpy import env
def shp2raster(year):
    print year
    # Set environment settings
    env.workspace = "F:/out/Feature/"
    indicators = ["IJI", "PAFRAC", "DIVISION", "CONTAG", "SHEI", "SHDI"]
    # Set local variables
    inFeature = str(year) + ".shp"
    for indicator in indicators:
        outRaster = "F:/out/Raster/" + indicator + "/" + str(year) + ".tif"
        cellSize = 3000
        field = indicator

        # Execute FeatureToRaster
        arcpy.FeatureToRaster_conversion(inFeature, field, outRaster, cellSize)
if __name__ == '__main__':
    years = [2014]
    for year in years:
        shp2raster(year)
