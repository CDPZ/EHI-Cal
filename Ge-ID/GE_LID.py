# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 23:56:32 2020

@author: cdpz
"""
import pandas as pd

path = 'Q:/NEW(1)/CSV/'


def GE_ID(pa_csv):
    df = pd.read_csv(pa_csv,header=0)
# =============================================================================
#     df.iloc[5][0] = df.iloc[5][0][df.iloc[5][0].rfind("/") + 1:df.iloc[5][0].find(".")]
# =============================================================================

    count = 0
    temp = df.shape[0]
    for i in range(df.shape[0]):
        if (temp-count) == i:
            break
        elif df.iloc[i][0] == "LID ":
            df.drop(index = i + count, axis = 0, inplace = True)
            df.iloc[i][0] = df.iloc[i][0][df.iloc[i][0].rfind("/") + 1:df.iloc[i][0].find(".")]
            count = count + 1
            continue
        else:
            df.iloc[i][0] = df.iloc[i][0][df.iloc[i][0].rfind("/") + 1:df.iloc[i][0].find(".")]
 
    df.to_csv(pa_csv, index=False)
    print("ok")

if __name__ == '__main__':
    years = [2002]
    for year in years:
        pa_csv = path + str(year) + ".csv"
        GE_ID(pa_csv)
