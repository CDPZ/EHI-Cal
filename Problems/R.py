# -*- coding: utf-8 -*-
import os
import subprocess
import multiprocessing as mp

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
    path = root + "/Folder " + str(99)
    paths.append(path)
    path = root + "/Folder " + str(96)
    paths.append(path)
    path = root + "/Folder " + str(79)
    paths.append(path)
    path = root + "/Folder " + str(102)
    paths.append(path)
    path = root + "/Folder " + str(103)
    paths.append(path)
    path = root + "/Folder " + str(98)
    paths.append(path)
    path = root + "/Folder " + str(78)
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
    years = [2006]
    for year in years:
        print ("will be running "+str(year)+ "\n")

        print ("gepa_succ")
        Frg(year)
