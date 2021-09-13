# -*- coding: utf-8 -*-
import os
import subprocess
import multiprocessing as mp



def gera_pathfbt(year):
    names = []


    names.append(str(107))

    names.append(str(115))

    for name in names:
        clip = "C:/research/NEW(1)/" + str(year) + "/Folder " + name
        clip_save = "F:/out/" + str(year) + "/Folder " + name
        more = ",x,999,x,x,1,x,IDF_GeoTIFF"
        count = 0
        pathlist = os.listdir(clip)
        i = 0
        while(True):                   #This time we change to 900, for the fragstats showed overflow error when running folder 5.
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
            i = i + 1
            if len(pathlist) < 2000:
                break
        clipf = open(clip_save + "/_" + str(i) + ".fbt", 'w+')
        for line in pathlist:
            (filename, extension) = os.path.splitext(line)
            if (extension == ".tif"):
                clipf.write(clip + '/' + line + more + '\n')


def run(path,j):
    FBTs = []
    for i in range(100):
        if os.path.isfile(path + "/_" + str(i) + ".fbt") is True:
            FBTs.append("_" + str(i) + ".fbt")
        else:
            break
    for fbt in FBTs:
        print (fbt)
        os.chdir(path)
        out = path +"/fragout" + fbt[1:-4]
        fca = "F:/fras/unnamed" + str(j) + ".fca"
        task = subprocess.Popen('frg -m '+ fca +' -b '+ fbt + ' -o ' + "\"" + out + "\"", stdout = subprocess.PIPE, shell = True)
        print(task.stdout.read())


def Frg(year):
    root = "F:/out/"+str(year)
    paths = []
    for i in [107,115]:
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
    years = [2002]
    for year in years:
        print ("will be running "+str(year)+ "\n")
        gera_pathfbt(year)

        print ("gepa_succ")
        Frg(year)
