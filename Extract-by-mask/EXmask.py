# -*- coding: utf-8 -*-
import os
import multiprocessing as mp
import arcpy
import psutil

import time

# 生成包含测试路径的list
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
    for i in range(119):  # 文件夹个数110
        if i == 0:
            continue
        elif i < 10:
            path = "F:/sub/Folder 0" + str(i)
            paths.append(path)
        else:
            path = "F:/sub/Folder " + str(i)    #E:/Cgrid_/
            paths.append(path)
    return paths



# 生成每个文件夹下各一个记录了自己所包含的shp路径的txt
def gera_fraction_shp_path(paths):
    for path in paths:
        clipf = open(path + "/dir.txt", 'a+')
        ff = os.walk(path)
        for root, dirs, files in ff:
            for file in files:
                (filename, extension) = os.path.splitext(file)
                if extension == ".shp":
                    file = '/' + file
                    p_shp = root + file + '\n'
                    clipf.write(p_shp)



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
        print "no history of " + path
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
                out = "D:\\research\\" + str(year) + "\\" + path[7:] + "\\" + filename  # 将shp的名称作为tif输出时的名称    str(year)******************* path[14:]
                
                
                if flag.value == 0:
                    # print("OK")
                    try:
                        arcpy.gp.ExtractByMask_sa(raster, Inputfeature, out + ".tif")
                    except:
                        continue
                    # outExtractByMask = ExtractByMask(raster, Inputfeature)                  #另一种调用方式 需要from arcpy.sa import *
                    # outExtractByMask.save(out + ".tif")
                elif flag.value == 1:
                    # print("not ok")
                    check_out(path, year, filename)
        else:
            filename = filename[0:-1]
            if int(filename) < int(lastfilename):
                continue
            else:
                out = "D:\\research\\" + str(year) + "\\" + path[7:] + "\\" + filename + '_'  # 将shp的名称作为tif输出时的名称    str(year)******************* path[14:]
                if flag.value == 0:
                    # print("OK")
                    try:
                        arcpy.gp.ExtractByMask_sa(raster, Inputfeature, out + ".tif")
                    except:
                        continue
                elif flag.value == 1:
                    # print("not ok")
                    check_out(path, year, filename)
    if flag.value == 0:
        print path + " has finished!\n"


def Run(i,year,flag,mutex,state = 1):

    mpp = mp.Pool(processes=i)  # 创建进程池，进程数目为i
    if state == 1:
        file_list_all = gera_folder_path()
    elif state == 0:
        file_list_all = gera_test_path()
    else:
        print "State error!"
    for filelist in file_list_all:
        print filelist,year
        print "ok"
        mpp.apply_async(single, args=(filelist, year, flag))  # 非阻塞提交新任务

    mpp.close()  # 关闭进程池，意味着不再接受新的任务
    if i == 1:
        while (True):
            num = input("Input 1 to save and quit\n")
            try:
                if num == 1:
                    mutex.acquire()
                    flag.value = 1
                    mutex.release()
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


def RUNWHOLE():
    years = [2008]#2007-30
    for year in years:
        begin_time = time.time()
        mutex = mp.Lock()
        # 供主进程传递保存指令给子进程，0为正常运行，1为开始保存
        flag = mp.Manager().Value('i', 0)  # flag类型是ctypes.c_long，不是普通的int

        print mp.cpu_count()  # 逻辑内核数
        print psutil.cpu_count(False)  # 物理内核数
        print "will be running "+str(year)+ "\n"

        Run(psutil.cpu_count(False),year,flag,mutex)

        end_time = time.time()
        print(end_time - begin_time)
if __name__ == '__main__':
    RUNWHOLE()
    
















# 准备工作，生成全部shp的路径并储存为文件，但后来发现好像没有用上
# def gera_whole_shp_path(paths):
#     f = open("E:/dirs" + ".txt", 'a+')
#     for path in paths:
#         ff = os.walk(path)
#         for root, dirs, files in ff:
#             for file in files:
#                 (filename, extension) = os.path.splitext(file)
#                 if extension == ".shp":
#                     file = '/' + file
#                     p_shp = root + file + '\n'
#                     f.write(p_shp)

# 读取一个路径文件，好像也没用上，被arcpy提供的arcpy.ListFeatureClasses()替代了。
# def walk(path):
#     file_list = []
#     with open(path + "/dir.txt", 'r') as f:
#         for line_t in f:
#             file_list.append(line_t)
#     return file_list


# 没用上，供子进程使用，得到自己工作文件夹下所有shp路径
# def get_my_shp_paths(path):
#     file_list = []
#     file_lists = []
#     file_list_ = walk(path)
#     for p_file in file_list_:
#         p_file = p_file.strip()
#         file_list.append(p_file)
#     file_lists.append(file_list)
#     return file_lists


# 没用上，读取所有shp路径
# def get_whole_shp_paths():
#     file_list_all = []
#     file_list_ = []
#
#     with open("E:" + "/dirs.txt", 'r') as f:
#         for line_t in f:
#             file_list_.append(line_t)
#     for p_file in file_list_:
#         p_file = p_file.strip()
#         file_list_all.append(p_file)
#     return file_list_all









# WRONG:：









# # 子进程调用，保存，生成或修改日志文件
# def check_out(path, year, filename):
#     if os.access(path + "/run.log", os.F_OK):  # 存在之前的日志文件
#         lines = []
#         check = 0
#         with open(path + "/run.log", 'r') as f:
#             for line_t in f:
#                 lines.append(line_t)
#         clipf = open(path + "/run.log", 'w+')
#         for line_t in lines:
#             if line_t[0] == year:
#                 string = str(year) + "," + filename
#                 print string
#                 clipf.write(string)
#                 check = 1
#             else:
#                 clipf.write(line_t)
#         if check == 0:
#             string = str(year) + "," + filename
#             print string
#             clipf.write(string)
#     else:  # 不存在
#         clipf = open(path + "/run.log", 'a+')
#         string = str(year) + "," + filename
#         print string
#         clipf.write(string)
#
#     print path + " has been saved!\n"
#
# #读取之前跑到的shp名，若本年没跑过则返回-1
# def readlog(path, year):
#     if os.access(path + "/run.log", os.F_OK):
#         with open(path + "/run.log", 'r') as f:
#             for line_t in f:
#                 if line_t[0] == year:
#                     return line_t[1]
#                 else:
#                     return -1
#     else:
#         return -1
