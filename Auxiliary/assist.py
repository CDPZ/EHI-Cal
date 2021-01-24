# -*- coding: utf-8 -*-
import os
import shutil

def gera_folder_path():
    paths = []
    for i in range(125):  # 文件夹个数124
        if i == 0:
            continue
        elif i < 10:
            path = "E:/Cgrid_/Folder 0" + str(i)
            paths.append(path)

        else:
            path = "E:/Cgrid_/Folder " + str(i)
            paths.append(path)
    return paths

def clear_log():
    file_list_all = gera_folder_path()
    for filelist in file_list_all:
        if os.access(filelist + "/run.log", os.F_OK):
            os.remove(filelist + '/run.log')

def del_file(path_data):
    for i in os.listdir(path_data):  # os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
        file_data = path_data + "\\" + i  # 当前文件夹的下面的所有东西的绝对路径
        if os.path.isfile(file_data) == True:  # os.path.isfile判断是否为文件,如果是文件,就删除.如果是文件夹.递归给del_file.
            os.remove(file_data)
        else:
            del_file(file_data)
def del_file_all(year):
    file_list_all = gera_folder_path()
    for filelist in file_list_all:
        del_file( "C:\\research\\NEW\\" + str(year) + "\\" + filelist[10:])

def multiply():


if __name__ == '__main__':
    year = 2002
    clear_log()
    del_file_all(year)

