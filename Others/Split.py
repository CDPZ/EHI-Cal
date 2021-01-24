import arcpy


if __name__ == '__main__':
    China = "D:/AAAAAAAAAA/China/Name.shp"
    in_polygon = "D:/AAAAAAAAAA/3KMfishnet.shp"

    arcpy.env.overwriteOutput = True

    arcpy.Split_analysis(China, in_polygon, "ID_1", "D:/AAAAAAAAAA/3KMout")
