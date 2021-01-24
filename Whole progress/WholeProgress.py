# -*- coding: utf-8 -*-
import os
import multiprocessing as mp
import arcpy
import psutil
import time
import pandas as pd
from arcpy import env


def gera_test_path():
    paths = []
    for i in range(73):  # 文件夹个数72
        if i == 0:
            continue
        elif i < 10:
            path = "E:/Cgrid_/tes/Folder 0" + str(i)
            paths.append(path)
        else:
            path = "E:/Cgrid_/tes/Folder " + str(i)
            paths.append(path)
    return paths


# 生成形如“E:/Cgrid_/Folder 01” ~ “E:/Cgrid_/Folder 124”的文件夹路径
def gera_folder_path():
    paths = []
    for i in range(111):  # 文件夹个数110
        if i == 0:
            continue
        elif i < 10:
            path = "Q:/sub/Folder 0" + str(i)
            paths.append(path)

        else:
            path = "Q:/sub/Folder " + str(i)    #E:/Cgrid_/
            paths.append(path)
    return paths



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
def single(path, year, flag):                                                                   # path 这个进程要跑的文件夹(124中的一个）， year本次工作的被裁栅格年份（2002~2015）
    # file_lists = []
    # file_lists = get_my_shp_paths(path)[0]

    arcpy.CheckOutExtension("spatial")                                                          # 权限检查
    arcpy.gp.overwriteOutput = 1                                                                # 裁出来的tif重复可覆盖
    raster = "C:\\research\\ESACCI-LC-L4-LCCS-Map-300m-P1Y-" + str(year) + "-v2.0.7.tif"        # 被裁的栅格影像所在目录
    arcpy.env.workspace = path                                                                  # 设置工作空间，以便调用listfeature
    shplist_1 = arcpy.ListFeatureClasses()                                                      # 读取工作空间内的要素类文件名（unicode）

    #上次跑到的shp序号,        同一数字序号的shp可能存在两份，其中一份末尾会有一个'_'   e.g."1.shp", "1_.shp"
    lastfilename = readlog(path, year)

    if lastfilename == -1:

        print "no history of " + path
    elif lastfilename[-1] == '_':
        lastfilename = lastfilename[0:-1]
        
    for Inputfeature in shplist_1:
        
        (filename, extension) = os.path.splitext(Inputfeature.encode('utf8'))                       # 获取shp的名称
        #同一数字序号的shp可能存在两份，其中一份末尾会有一个'_'   e.g."1.shp", "1_.shp"
        if filename[-1] != '_':
            if int(filename) < int(lastfilename):
                continue
            else:
                out = "C:\\research\\NEW(1)\\" + str(year) + "\\" + path[7:] + "\\" + filename      # 将shp的名称作为tif输出时的名称    str(year)******************* path[14:]
                if flag.value == 0:
                    # print("OK")
                    arcpy.gp.ExtractByMask_sa(raster, Inputfeature, out + ".tif")

                    # outExtractByMask = ExtractByMask(raster, Inputfeature)                         #另一种调用方式 需要from arcpy.sa import *
                    # outExtractByMask.save(out + ".tif")
                elif flag.value == 1:
                    # print("not ok")
                    check_out(path, year, filename)
        else:
            filename = filename[0:-1]
            if int(filename) < int(lastfilename):
                continue
            else:
                out = "C:\\research\\NEW(1)\\" + str(year) + "\\" + path[7:] + "\\" + filename + '_'  # 将shp的名称作为tif输出时的名称    str(year)******************* path[14:]
                if flag.value == 0:
                    # print("OK")
                    arcpy.gp.ExtractByMask_sa(raster, Inputfeature, out + ".tif")
                elif flag.value == 1:
                    # print("not ok")
                    check_out(path, year, filename)

    if flag.value == 0:
        print path + " has finished!\n"


def Run(i,year, flag,state = 1):
    mpp = mp.Pool(processes=i)                                                     # 创建进程池，进程数目为i
    if state == 1:
        file_list_all = gera_folder_path()
    elif state == 0:
        file_list_all = gera_test_path()
    else:
        print "State error!"
    for filelist in file_list_all:
        mpp.apply_async(single, args=(filelist, year, flag))                       # 非阻塞提交新任务

    mpp.close()  # 关闭进程池，意味着不再接受新的任务
    if i == 1:
        while (True):
            num = input("Input 1 to save and quit\n")
            try:
                if num == 1:
                    flag.value = 1
                    print "trying to save progress\n"
                else:
                    print "illegal input\n"
            except Exception as ex:
                print ("表达式为空，请检查/loadingtimeout")
    else:
        mpp.join()
    print ("whole year finished with %d", i)


def testE(year):
    # list = range(mp.cpu_count())
    # list.reverse()
    for i in range(mp.cpu_count()):
        if i > 3:
            begin_time = time.time()
            Run (i, year, 0)
            end_time = time.time()
            print (end_time - begin_time)


#生成fbt文件以供计算
def gera_pathfbt(year):
    names = []

    for i in range(9):
        name = str(0) + str(i + 1)
        names.append(name)

    for i in range(9, 111):
        name = str(i + 1)
        names.append(name)

    for name in names:
        clip = "C:/research/NEW(1)/" + str(year) + "/Folder " + name
        more = ",x,999,x,x,1,x,IDF_GeoTIFF"

        pathlist = os.listdir(clip)
        clipf = open(clip + "/_" + "1" + ".fbt", 'w+')
        for line in pathlist:
            (filename, extension) = os.path.splitext(line)
            if (extension == ".tif"):
                clipf.write(clip + '/' + line + more + '\n')


def RRRRRR(year):
    root = "C:/research/NEW(1)/"+str(year)
    paths = []
    for i in range(111):  # 文件夹个数124
        if i == 0:
            continue
        elif i < 10:
            path = root + "/Folder 0" + str(i)
            paths.append(path)

        else:
            path = root + "/Folder " + str(i)
            paths.append(path)
    for path in paths:
        os.chdir(path)
        out = path +"/fragout"
        fbt = "_1.fbt"
        fca = "C:/research/unnamed1.fca"
        os.system('frg -m '+ fca +' -b '+ fbt + ' -o ' + "\"" + out + "\"")

#用于指标计算完成后合并成一张一年的总表
def hebing(year):
    root = "C:/research/NEW(1)/" + str(year)
    paths = []
    for i in range(111):  # 文件夹个数124
        if i == 0:
            continue
        elif i < 10:
            path = root + "/Folder 0" + str(i) + "/fragout.land"
            paths.append(path)

        else:
            path = root + "/Folder " + str(i) + "/fragout.land"
            paths.append(path)


    for land in paths:
        fr = open(land,'r').read()
        with open('C:/research/NEW(1)/CSV/' + str(year) + '.csv', 'a') as f:
            f.write(fr)
    print(u'合并完毕！')


#之前以为_和不带_的是重复的所以想删掉来着，后来发现不是+-+
def quchong(file):
    df = pd.read_csv(file,header=0)
    datalist = df.drop_duplicates()
    datalist.to_csv(file)



#将算出来结果的LID算出来
def GE_ID(pa_csv,year):
    df = pd.read_csv(pa_csv, header=0)
    # =============================================================================
    #     df.iloc[5][0] = df.iloc[5][0][df.iloc[5][0].rfind("/") + 1:df.iloc[5][0].find(".")]
    # =============================================================================

    count = 0
    temp = df.shape[0]
    for i in range(df.shape[0]):
        if (temp - count) == i:
            break
        elif df.iloc[i][0] == "LID ":
            df.drop(index=i + count, axis=0, inplace=True)
            df.iloc[i][0] = df.iloc[i][0][df.iloc[i][0].rfind("/") + 1:df.iloc[i][0].find(".")]
            count = count + 1
            continue
        else:
            df.iloc[i][0] = df.iloc[i][0][df.iloc[i][0].rfind("/") + 1:df.iloc[i][0].find(".")]

    df.to_csv(pa_csv, index=False)
    print("ok")

def shp2Raster(year):
    # Set environment settings
    env.workspace = "C:/research/NEW(1)/Feature/"
    indicators = ["IJI", "PAFRAC", "DIVISION", "CONTAG", "SHEI", "SHDI"]
    # Set local variables
    inFeature = str(year) + ".shp"
    for indicator in indicators:
        outRaster = "C:/research/NEW(1)/Raster/" + indicator + "/"+ str(year) + ".tif"
        cellSize = 3000
        field = indicator

        # Execute FeatureToRaster
        arcpy.FeatureToRaster_conversion(inFeature, field, outRaster, cellSize)
if __name__ == '__main__':

    years = [2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]
    for year in years:
        # 供主进程传递保存指令给子进程，0为正常运行，1为开始保存
        flag = mp.Manager().Value('i', 0)  # flag类型是ctypes.c_long，不是普通的int

        print mp.cpu_count()  # 逻辑内核数
        print psutil.cpu_count(False)  # 物理内核数
        print "will be running "+str(year)+ "\n"

        Run(psutil.cpu_count(False),year,flag)


        gera_pathfbt(year)
        RRRRRR(year)
        hebing(year)
        path = 'C:/research/NEW(1)/CSV/'
        pa_csv = path + str(year) + ".csv"
        GE_ID(pa_csv, year)

#        shp2Raster(year)



# 生成每个文件夹下各一个记录了自己所包含的shp路径的txt
# def gera_fraction_shp_path(paths):
#     for path in paths:
#         clipf = open(path + "/dir.txt", 'a+')
#         ff = os.walk(path)
#         for root, dirs, files in ff:
#             for file in files:
#                 (filename, extension) = os.path.splitext(file)
#                 if extension == ".shp":
#                     file = '/' + file
#                     p_shp = root + file + '\n'
#                     clipf.write(p_shp)
