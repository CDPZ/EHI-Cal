# -*- coding: utf-8 -*-
import os
import multiprocessing as mp
import arcpy
import psutil

#读取之前跑到的shp名，若本年没跑过则返回-1
def readlog(path, year):
    if os.access(path + "/run.log", os.F_OK):
        with open(path + "/run.log", 'r') as f:
            for line_t in f:
                print int(line_t[0:4])
                if int(line_t[0:4]) == year:
                    print "Last time run shp " + line_t[5:-1]
                    return line_t[5:-1]
                else:
                    return -1
    else:
        return -1




# 子进程调用，保存，生成或修改日志文件
def check_out(path, year, filename):
    if os.access(path + "/run.log", os.F_OK):  # 存在之前的日志文件
        lines = []
        check = 0
        with open(path + "/run.log", 'r') as f:
            for line_t in f:
                lines.append(line_t)
        clipf = open(path + "/run.log", 'w+')
        for line_t in lines:
            if int(line_t[0:4]) == year:
                string = str(year) + "," + filename + '\n'
                print string
                clipf.write(string)
                check = 1
            else:
                clipf.write(line_t)
        if check == 0:
            string = str(year) + "," + filename + '\n'
            print string
            clipf.write(string)
    else:  # 不存在
        clipf = open(path + "/run.log", 'a+')
        string = str(year) + "," + filename + '\n'
        print string
        clipf.write(string)

    print path + " has been saved!\n"


# 进程函数
def single(path, year, flag):  # path 这个进程要跑的文件夹(124中的一个）， year本次工作的被裁栅格年份（2002~2015）
    # file_lists = []
    # file_lists = get_my_shp_paths(path)[0]

    arcpy.CheckOutExtension("spatial")  # 权限检查
    arcpy.gp.overwriteOutput = 1  # 裁出来的tif重复可覆盖
    raster = "C:\\research\\ESACCI-LC-L4-LCCS-Map-300m-P1Y-" + str(year) + "-v2.0.7.tif"  # 被裁的栅格影像所在目录
    arcpy.env.workspace = path  # 设置工作空间，以便调用listfeature
    shplist_1 = arcpy.ListFeatureClasses()  # 读取工作空间内的要素类文件名（unicode）

    #上次跑到的shp序号,        同一数字序号的shp可能存在两份，其中一份末尾会有一个'_'   e.g."1.shp", "1_.shp"
    lastfilename = readlog(path, year)
    if lastfilename == -1:
        print "no history of " + path + str(year)
    elif lastfilename[-1] == '_':
        lastfilename = lastfilename[0:-1]



    for Inputfeature in shplist_1:

        (filename, extension) = os.path.splitext(Inputfeature.encode('utf8'))  # 获取shp的名称
        filename = filename[11:]
        #同一数字序号的shp可能存在两份，其中一份末尾会有一个'_'   e.g."1.shp", "1_.shp"
        if filename[-1] != '_':
            if int(filename) < int(lastfilename):
                continue
            else:
                out = "C:\\research\\NEW(1)\\" + str(year) + "\\" + path[7:] + "\\" + filename  # 将shp的名称作为tif输出时的名称
                if flag == 0:
                    print("OK")
                    try:
                        arcpy.gp.ExtractByMask_sa(raster, Inputfeature, out + ".tif")
                    except:
                        continue
                    # outExtractByMask = ExtractByMask(raster, Inputfeature)                  #另一种调用方式 需要from arcpy.sa import *
                    # outExtractByMask.save(out + ".tif")
                elif flag == 1:
                    print("not ok")
                    check_out(path, year, filename)
        else:
            filename = filename[0:-1]
            if int(filename) < int(lastfilename):
                continue
            else:
                out = "C:\\research\\NEW(1)\\" + str(year) + "\\" + path[7:] + "\\" + filename + '_'  # 将shp的名称作为tif输出时的名称
                if flag == 0:
                    print("OK")
                    try:
                        arcpy.gp.ExtractByMask_sa(raster, Inputfeature, out + ".tif")
                    except:
                        continue
                elif flag == 1:
                    print("not ok")
                    check_out(path, year, filename)

    if flag == 0:
        print path + " has finished!\n"


if __name__ == '__main__':

    year = 2002
    path = "Q:\\sub\\Folder 06"
    # 供主进程传递保存指令给子进程，0为正常运行，1为开始保存
    flag = 0

    print mp.cpu_count()  # 逻辑内核数
    print psutil.cpu_count(False)  # 物理内核数
    print "will be running 2002\n"

    single(path, year, flag)








