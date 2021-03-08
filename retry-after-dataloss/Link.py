import arcpy
import pandas as pd
import time

shppath = "F:\\NEW(1)\\Feature\\fineinter.shp"
csvpath = "F:\\NEW(1)\\CSV\\2003.csv"
count = 0
percent = 0
if __name__ == '__main__':
    data = pd.read_csv(csvpath)
    #data.sort_values("LID", inplace=True)
    cursor = arcpy.UpdateCursor(shppath,"","","","id_fine_wh A")
    print ("start...")
    for row in cursor:
        The_Line = data[data.LID == row.id_fine_wh]

        
        The_Index = The_Line.index

        try:
            IJI = The_Line.loc[The_Index, ' IJI']
        except:
            IJI = 0
        try:
            row.IJI = float(IJI)
        except:
            row.IJI = 0


        try:
            PAFRAC = The_Line.loc[The_Index, ' PAFRAC']
        except:
            PAFRAC = 0
        try:
            row.PAFRAC = float(PAFRAC)
        except:
            row.PAFRAC = 0


        try:
            SHEI = The_Line.loc[The_Index, ' SHEI']
        except:
            SHEI = 0
        try:
            row.SHEI = float(SHEI)
        except:
            row.SHEI = 0


        try:
            SHDI = The_Line.loc[The_Index, ' SHDI']
        except:
            SHDI = 0
        try:
            row.SHDI = float(SHDI)
        except:
            row.SHDI = 0


        try:
            DIVISION = The_Line.loc[The_Index, ' DIVISION']
        except:
            DIVISION = 0
        try:
            row.DIVISION = float(DIVISION)
        except:
            row.DIVISION = 0


        try:
            CONTAG = The_Line.loc[The_Index, ' CONTAG']
        except:
            CONTAG = 0
        try:
            row.CONTAG = float(CONTAG)
        except:
            row.CONTAG = 0
        count += 1
        start =time.clock()
        cursor.updateRow(row)
        end = time.clock()
        print('Running time: %s Seconds'%(end-start))
        

        if(int(round(count/10000))) == percent:
            print "percent: %d%%" % (percent,)
            percent += 1

    print("yes")
