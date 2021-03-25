#coding=utf-8# 
import os
path = "F:\sta_sub\dup.csv"


def walkFile(dup):
    IDs = []
    ID_dup = []
    print("start_2_rem")
    for root, dirs, files in os.walk("D:/Users/Desktop/"):
        for f in files:
            # print(os.path.join(root, f))
            
            (filename, extension) = os.path.splitext(f)
            print root,dirs,f
            if filename+"\n" in dup:
                os.remove(root +"/"+ f)



if __name__ == '__main__':
    dup = []
    with open(path, "r") as f:
        for id in f:
            if id in dup:
                continue
            else:

                dup.append(id)
    walkFile(dup)
