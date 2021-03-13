# -*- coding: utf-8 -*-
import arcpy

shp_path = "F:/fineinter.shp"
if __name__ == '__main__':
    cursor = arcpy.UpdateCursor(shp_path,"","","","id_fine_wh A")
    print ("start...")
    IDs = []
    for row in cursor:
        if row.id_fine_wh not in IDs:
            IDs.append(row.id_fine_wh)
            print row.id_fine_wh
        cursor.updateRow(row)
    print 'saving...'
    with open("F:\sta_sub\sta_shp.csv", 'w') as f:
        for ID in IDs:
            f.write(str(ID))
            f.write('\n')