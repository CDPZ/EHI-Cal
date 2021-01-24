# Import system modules
import arcpy
from arcpy import env
def shp2raster(year):
        
    # Set environment settings
    env.workspace = "C:/research/NEW/Feature/"
    indicators = ["IJI", "PAFRAC", "DIVISION", "CONTAG", "SHEI", "SHDI"]
    # Set local variables
    inFeature = str(year) + ".shp"
    for indicator in indicators:
        outRaster = "C:/research/NEW/Raster/" + indicator + "/" + str(year) + ".tif"
        cellSize = 3000
        field = indicator

        # Execute FeatureToRaster
        arcpy.FeatureToRaster_conversion(inFeature, field, outRaster, cellSize)
if __name__ == '__main__':
    years = [2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]
    for year in years:
        shp2raster(year)
