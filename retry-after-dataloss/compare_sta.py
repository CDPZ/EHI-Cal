# -*- coding: utf-8 -*-

import os


if __name__ == '__main__':
    IDs = []
    IDw = []
    with open("F:\sta_sub\sta_.csv", 'r') as f:
        for ID in f:
            IDs.append(ID)
    with open("F:\sta_sub\sta_shp.csv", 'r') as f_:
        for ID in f_:
            if ID not in IDs:
                IDw.append(ID)
    with open("F:\sta_sub\diff.csv", 'w') as f:
        for ID in IDw:
            f.write(ID)
            f.write('\n')