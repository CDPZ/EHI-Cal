# -*- coding: utf-8 -*-
import os
import shutil


def del_file(path_data):
    for i in os.listdir(path_data):  # os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
        file_data = path_data + "\\" + i  # 当前文件夹的下面的所有东西的绝对路径

        print (file_data)
        if os.path.isfile(file_data) == True:  # os.path.isfile判断是否为文件,如果是文件,就删除.如果是文件夹.递归给del_file.
            if os.path.splitext(i)[1]== ".fbt"and os.path.splitext(i)[0]== "_1":
                os.remove(file_data)
        else:
            del_file(file_data)



if __name__ == '__main__':
    path_data = u"C:\\research\\NEW(1)"
    del_file(path_data)



#for i in range(69,110):
#...     file_data = u"C:\\research\\NEW(1)\\2002\\Folder " + str(i) + "\\_1.fbt"
##...     if os.path.isfile(file_data) == True:
#...             os.remove(file_data)


