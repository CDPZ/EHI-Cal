import arcpy


if __name__ == '__main__':
    China = "D:/DaTa/Yangtz/workflow/shape_ehi/fishnet/3.shp"
    in_polygon = "D:/DaTa/Yangtz/workflow/shape_ehi/fishnet/3.shp"

    arcpy.env.overwriteOutput = True

    arcpy.Split_analysis(China, in_polygon, "idj", "D:/DaTa/Yangtz/workflow/shape_ehi/sp_/3/")
