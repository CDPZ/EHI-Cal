#coding=utf-8
import arcpy
import os
# 获取当前路径
currentPath=os.getcwd()
print currentPath
# 遍历当前路径
files=os.listdir(currentPath)
for file in files:
    # 判断是否为文件夹
    if(len(file.split('.'))<2):
        # 设置工作空间
        arcpy.env.workspace=currentPath+"\\"+file
        print file
        # 判断select+文件夹否存在,不存在则新建
        if not os.path.exists(currentPath+'\\'+'select'+file):
            os.mkdir(currentPath+'\\'+'select'+file)
        # 遍历文件夹
        shpFiles=os.listdir(file)
        for shpFile in shpFiles:
            # 判断是否为shp文件
            if(shpFile.split('.')[-1]=="shp"):
                inPoint=shpFile
                outPoint=currentPath+'\\'+'select'+file+'\\'+shpFile[1:11]+".shp"
                print inPoint
                lyr=shpFile[1:11]
                arcpy.MakeFeatureLayer_management(inPoint, lyr)
                arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION", '"date" LIKE \'%00:00\'')
                arcpy.CopyFeatures_management(lyr, outPoint)
