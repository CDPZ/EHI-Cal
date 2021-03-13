#coding=utf-8
import arcpy
import os

if __name__ == '__main__':
    DIFFS = []
    with open ("F:\\sta_sub\\dup\\dup1.csv",'r') as f:
        for diff in f:
            if len (diff[0:-1]) > 0:
                DIFFS.append(diff[0:-1])
    arcpy.MakeFeatureLayer_management("F:\\fineinter.shp", "fine")
    for diff in DIFFS:

        arcpy.SelectLayerByAttribute_management("fine", "NEW_SELECTION", '"id_fine_wh"='+diff[11:])
        arcpy.CopyFeatures_management("fine", "F:\\sta_sub\\dup\\dup1"+diff[11:]+'.shp')
