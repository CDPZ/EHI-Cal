import arcpy


if __name__ == '__main__':
    China = "D:/DaTa/csj_whole/attempt_/PART/New_Shapefile_Intersect2.shp"
    in_polygon = "D:/DaTa/csj_whole/attempt_/PART/New_Shapefile_Intersect2.shp"

    arcpy.env.overwriteOutput = True

    arcpy.Split_analysis(China, in_polygon, "SID", "D:/DaTa/csj_whole/attempt_/PART/raw/2")
