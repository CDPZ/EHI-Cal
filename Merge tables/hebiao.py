# -*- coding: utf-8 -*-


def hebing(year):
    root = "C:/research/NEW/" + str(year)
    paths = []
    for i in range(125):  # 文件夹个数124
        if i == 0:
            continue
        elif i < 10:
            path = root + "/Folder 0" + str(i) + "/fragout.land"
            paths.append(path)

        else:
            path = root + "/Folder " + str(i) + "/fragout.land"
            paths.append(path)


    for land in paths:
        fr = open(land,'r').read()
        with open('C:/research/NEW/CSV/' + str(year) + '.csv', 'a') as f:
            f.write(fr)
    print(u'合并完毕！')


if __name__ == '__main__':
    years = [2006,2007,2008,2014,2015]
    for year in years:
        hebing(year)

