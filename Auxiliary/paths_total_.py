# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:55:38 2019

@author: 22879
"""

import os

names = []

for i in range(9):
    name = str(0) + str(i + 1) 
    names.append(name)

for i in range(9,110):
    name =  str(i + 1) 
    names.append(name)



for name in names:
    clip="C:/research/NEW(1)/2002/Folder " + name
    more=",x,999,x,x,1,x,IDF_GeoTIFF"
    paths=clip
    pathlist=os.listdir(paths)
    file=[]

    count=1000
    for line in pathlist:
        (filename, extension) = os.path.splitext(line)
        if (extension==".tif"):
            if(count==1000):
                clipf=open(clip+"/_" + str(int(count/1000))+ ".fbt",'w+')
            clipf.write(paths+'/'+line+more+'\n')
            count+=1

