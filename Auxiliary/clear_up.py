# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 14:23:52 2020

@author: cdpz
"""
import shutil
import os


def take_out(name, extensions):
    pack = []
    for extension in extensions:
        pack.append(name + extension)
    return pack


def walk(path):
    count = 0
    for i in range(12,24):
        ff = os.walk(path + "/" + str(i+1))
        time = 0
        extensions = []
        packs = []
        last = "0"
        for root, dirs, files in ff:
            for file in files:
                if file[3] == 'j' or file[1] == 'n':
                    continue
                (filename, extension) = os.path.splitext(file)
                if time == 0:
                    time += 1
                    extensions.append(extension)
                    last = filename
                    continue
                elif list(filename) == list(last):
                    time += 1
                    extensions.append(extension)
                    continue
                elif time == 4:
                    packs.append(take_out(last, extensions))
                    count += 1
                    gefl(root,count,packs)
                    time = 0
                    packs = []

                    extensions = []
                    time += 1
                    extensions.append(extension)
                    last = filename
                elif time < 4:
                    print(last)
                    time = 0
                    extensions = []
                    time += 1
                    extensions.append(extension)
                else:
                    print("time = ")
                    print(time)
                    print("logic missed.")
                    os.system("pause")
                    time = 0
                    extensions = []
                    time += 1
                    extensions.append(extension)
            if time == 4:
                packs.append(take_out(last, extensions))
                count += 1
                gefl(root,count,packs)
                time = 0
                packs = []

                extensions = []
            elif time < 4:
                print(last)
                time = 0
                extensions = []
            else:
                print("time = ")
                print(time)
                print("logic missed.")
                os.system("pause")
                time = 0
                extensions = []

def gefl(path,count,packs):
#    print packs[0],count
    cur_fl = count / 10000 + 61
    if cur_fl < 10:
        des_path = "D:/AAAAAAAAAA/3KMSave/Folder 0" + str(int(cur_fl))
        if not os.path.isdir(des_path):
            os.mkdir(des_path)
    else:
        des_path = "D:/AAAAAAAAAA/3KMSave/Folder " + str(int(cur_fl))
        if not os.path.isdir(des_path):
            os.mkdir(des_path)
    for single in packs[0]:
        shutil.copy(path + '/' + single, des_path + '/')

if __name__ == '__main__':
    ger_path = "Q:/subwhsp"
    walk(ger_path)

