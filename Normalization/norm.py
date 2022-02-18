# -*- coding: utf-8 -*-
import arcpy
import pandas as pd
import numpy as np



shppath = "D:\\User\\Desktop\\Feature\\"

count = 0
percent = 0
def loadshp():
    ally = list()
    siny = list()
    for year in range(2002,2016):
        cursor = arcpy.SearchCursor(shppath + str(year) + ".shp", ["id_fine_wh A", "SHEI"])
        for row in cursor:
            siny.append(row.SHEI)
        ally.append(siny)
    return ally

def cal_std(ally):
    std = list()
    sum_ally = 0
    for a in ally:
        for b in a:
            sum_ally += b

    # n_ally = np.array(ally)
    # a_mean = np.mean(n_ally)
    # a_std = np.std(n_ally,ddof=1)
    
    return sum_ally#, a_mean, a_std

def draw_sing_scatter(ally):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    reload(sys) 
    sys.setdefaultencoding('utf-8')

    x = range(100)
    y = ally[0][:100]
    plt.plot(x,y)

if __name__ == '__main__':
    ally = loadshp()
    draw_sing_scatter(ally)
    sum_  = cal_std(ally)    #mean_shei,std_shei
    print sum_