# -*- coding: utf-8 -*-
import os
from subprocess import run

root = "C:/research/NEW(1)/2015"

def gera_pathfbt(year):
    names = []

    for i in range(4,9):
        name = str(0) + str(i + 1)
        names.append(name)

    for i in range(9, 110):
        name = str(i + 1)
        names.append(name)

    for name in names:

        clip = "C:/research/NEW(1)/" + str(year) + "/Folder " + name
        more = ",x,999,x,x,1,x,IDF_GeoTIFF"
        count = 0
        pathlist = os.listdir(clip)
        for i in range(int(len(pathlist)/1000)):
            clipf = open(clip + "/_" + str(i) + ".fbt", 'w+')
            for line in pathlist:
                (filename, extension) = os.path.splitext(line)
                if (extension == ".tif"):
                    clipf.write(clip + '/' + line + more + '\n')
                    count += 1
                    if count/1000==1:
                        pathlist = pathlist[1000:]
                        count = 0
                        break



def Frg(year):
    root = "C:/research/NEW(1)/"+str(year)
    paths = []
    for i in range(110):  # 文件夹个数124
        if i == 0:
            continue
        elif i < 10:
            path = root + "/Folder 0" + str(i)
            paths.append(path)

        else:
            path = root + "/Folder " + str(i)
            paths.append(path)

    for path in paths:
        FBTs = []
        for i in range(200):
            if os.path.isfile(path + "/_" + str(i) + ".fbt") is True:
                FBTs.append("_" + str(i) + ".fbt")
            else:
                break
        for fbt in FBTs:
            os.chdir(path)
            out = path +"/fragout" + fbt[1:-4]
            fca = "C:/research/unnamed14.fca"
            run('frg -m '+ fca +' -b '+ fbt + ' -o ' + "\"" + out + "\"", shell = True)



        
if __name__ == '__main__':
    years = [2015]
    for year in years:
        print ("will be running "+str(year)+ "\n")
        gera_pathfbt(year)
        Frg(year)
