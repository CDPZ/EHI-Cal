# -*- coding: utf-8 -*-
import os
import subprocess
import multiprocessing as mp

root = "C:/research/NEW(1)/2015"

def gera_pathfbt(year):
    names = []

    for i in range(9):
        name = str(0) + str(i + 1)
        names.append(name)

    for i in range(9, 110):
        name = str(i + 1)
        names.append(name)

    for name in names:

        clip = "C:/research/NEW(1)/" + str(year) + "/Folder " + name
        clip_save = "Q:/NEW(1)/" + str(year) + "/Folder " + name
        more = ",x,999,x,x,1,x,IDF_GeoTIFF"
        count = 0
        pathlist = os.listdir(clip)
        for i in range(int(len(pathlist)/1000)):
            clipf = open(clip_save + "/_" + str(i) + ".fbt", 'w+')
            for line in pathlist:
                (filename, extension) = os.path.splitext(line)
                if (extension == ".tif"):
                    clipf.write(clip + '/' + line + more + '\n')
                    count += 1
                    if count/1000==1:
                        pathlist = pathlist[1000:]
                        count = 0
                        break

def run(path,j):
    FBTs = []
    for i in range(200):
        if os.path.isfile(path + "/_" + str(i) + ".fbt") is True:
            FBTs.append("_" + str(i) + ".fbt")
        else:
            break
    for fbt in FBTs:
        os.chdir(path)
        out = path +"/fragout" + fbt[1:-4]
        fca = "C:/research/unnamed" + str(j) + ".fca"
        task = subprocess.Popen('frg -m '+ fca +' -b '+ fbt + ' -o ' + "\"" + out + "\"", stdout = subprocess.PIPE, shell = True)
        print(task.stdout.read())


def Frg(year):
    root = "Q:/NEW(1)/"+str(year)
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
    mpp = mp.Pool(processes=7)
    count = 0
    for path in paths:
        count += 1
        mpp.apply_async(run, args=(path, count%7))  # 非阻塞提交新任务
    mpp.close()  
    mpp.join()
    print ("whole year finished")


    
if __name__ == '__main__':
    years = [2002]
    for year in years:
        print ("will be running "+str(year)+ "\n")
        gera_pathfbt(year)
        Frg(year)
