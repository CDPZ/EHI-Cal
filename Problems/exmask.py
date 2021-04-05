# -*- coding: utf-8 -*-
import os
import arcpy



# 进程函数
def single(path, year):  # path 这个进程要跑的文件夹(124中的一个）， year本次工作的被裁栅格年份（2002~2015）
    # file_lists = []
    # file_lists = get_my_shp_paths(path)[0]

    arcpy.CheckOutExtension("spatial")  # 权限检查
    arcpy.gp.overwriteOutput = 1  # 裁出来的tif重复可覆盖
    raster = "C:\\research\\ESACCI-LC-L4-LCCS-Map-300m-P1Y-" + str(year) + "-v2.0.7.tif"  # 被裁的栅格影像所在目录
    arcpy.env.workspace = path  # 设置工作空间，以便调用listfeature
    shplist_1 = arcpy.ListFeatureClasses()  # 读取工作空间内的要素类文件名（unicode）

    #上次跑到的shp序号,        同一数字序号的shp可能存在两份，其中一份末尾会有一个'_'   e.g."1.shp", "1_.shp"

    for Inputfeature in shplist_1:

        (filename, extension) = os.path.splitext(Inputfeature.encode('utf8'))  # 获取shp的名称
        filename = filename[11:]
        #同一数字序号的shp可能存在两份，其中一份末尾会有一个'_'   e.g."1.shp", "1_.shp"
        if filename[-1] != '_':
            out = "D:\\research\\" + str(year) + "\\" + path[7:] + "\\" + filename  # 将shp的名称作为tif输出时的名称    str(year)******************* path[14:]
            try:
                arcpy.gp.ExtractByMask_sa(raster, Inputfeature, out + ".tif")
            except:
                continue
        else:
            filename = filename[0:-1]


            out = "D:\\research\\" + str(year) + "\\" + path[7:] + "\\" + filename + '_'  # 将shp的名称作为tif输出时的名称    str(year)******************* path[14:]

            try:
                arcpy.gp.ExtractByMask_sa(raster, Inputfeature, out + ".tif")
            except:
                continue
    print path + " has finished!\n"

if __name__ == '__main__':

    year = 2010
    for i in [68,61,70,71,73,74,75,69]:
        path = "F:\\sub\\Folder " + str(i)
        # 供主进程传递保存指令给子进程，0为正常运行，1为开始保存

        print "will be running " + str(i) + "\n"

        single(path, year)

