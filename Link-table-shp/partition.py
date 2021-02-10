import pandas as pd
import math

pa_csv = "F:\\NEW(1)\\CSV\\2002.csv"
if __name__ == '__main__':
    df =pd.read_csv(pa_csv)
    rows,cols=df.shape
    split_num =10
    value =math.floor(rows/split_num)
    rows_format =value*split_num
    new_list =[[i,i+split_num] for i in range(0,rows_format,split_num)]

    for i_j in new_list:
        i,j =i_j
        excel_small =df[i:j]
        excel_small.to_excel('2015-2017_RADI_{0}_{1}.xls'.format(i,j),index=False)
        df[rows_format:].to_excel('2015-2017_RADI_last.xls')
        

