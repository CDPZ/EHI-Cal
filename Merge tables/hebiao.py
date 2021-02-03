# -*- coding: utf-8 -*-

import os

def hebing(year):
    root = "F:/NEW(1)/" + str(year)
    paths = []
    for i in range(111):  # 文件夹个数124
        if i == 0:
            continue
        elif i < 10:
            for j in range(400):
                path = root + "/Folder 0" + str(i) + "/fragout"+ str(j) +".land"
                if os.path.isfile(path):
                    paths.append(path)
                else:
                    break

        else:
            for j in range(400):
                path = root + "/Folder " + str(i) + "/fragout"+ str(j) +".land"
                if os.path.isfile(path):
                    paths.append(path)
                else:
                    break


    for land in paths:
        fr = open(land,'r').read()
        with open('F:/NEW(1)/CSV/' + str(year) + '.csv', 'a') as f:
            f.write(fr)
    print(u'合并完毕！')


if __name__ == '__main__':
    years = [2003]
    for year in years:
        hebing(year)

