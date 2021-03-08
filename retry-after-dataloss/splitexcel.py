# -*- coding: utf-8 -*-
import csv
import os
import pandas as pd
 
def split_csv(path):
    home_path = "F:\\NEW(1)\\CSV\\2002"
    total_len = len(open(path,'r').readlines())  
    file_num = (int)(round(total_len / 30000) + 1)

    data = pd.read_csv(path)
    print(u"总行数: " +str(data.shape[0]))
    
    for i in range(file_num):
        if i == file_num - 1:
            save_data = data.iloc[i*30000::]
        else:
            save_data = data.iloc[i*30000:i * 30000 + 30000]
        save_data.to_excel(home_path + "\\" + str(i) + ".xls", index = False) 
    

 
 
 
if __name__ == '__main__':
    path = 'F:\\NEW(1)\\CSV\\2002.csv'
    
    split_csv(path)