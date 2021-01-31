# -*- coding: utf-8 -*-
import os
import subprocess
import multiprocessing as mp



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
        for i in range(int(len(pathlist)/400)):                   #This time we change to 900, for the fragstats showed overflow error when running folder 5.
            clipf = open(clip_save + "/_" + str(i) + ".fbt", 'w+')
            for line in pathlist:
                (filename, extension) = os.path.splitext(line)
                if (extension == ".tif"):
                    clipf.write(clip + '/' + line + more + '\n')
                    count += 1
                    if count/2000==1:
                        pathlist = pathlist[2000:]
                        count = 0
                        break
                else:
                    count += 1
                    if count/2000==1:
                        pathlist = pathlist[2000:]
                        count = 0
                        break

def run(path,j):
    FBTs = []
    for i in range(500):
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
    mpp.daemon = True
    count = 0
    for path in paths:
        count += 1
        mpp.apply_async(run, args=(path, count%7))  # 非阻塞提交新任务
    mpp.close()  
    mpp.join()
    print ("whole year finished")


    
if __name__ == '__main__':
    years = [2003]
    for year in years:
        print ("will be running "+str(year)+ "\n")
        gera_pathfbt(year)
        Frg(year)
