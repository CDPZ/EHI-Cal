import arcpy
import pandas as pd


shppath = "F:\\out\\Feature\\"
csvpath = "F:\\out\\CSV\\"
count = 0
percent = 0
if __name__ == '__main__':
    for year in [2008]:
        print (year)
        data = pd.read_csv(csvpath + str(year) + "fkj.csv")
        #data.sort_values("LID", inplace=True)
        cursor = arcpy.UpdateCursor(shppath + str(year) + ".shp","","","","id_fine_wh A")
        print ("start...")
        
        for row in cursor:
            if int(row.IJI)|int(row.PAFRAC)|int(row.SHEI)|int(row.SHDI)|int(row.CONTAG)|int(row.DIVISION) != 0:
                continue
            The_Line = data[data.LID == row.id_fine_wh]


            try:
                The_Index = The_Line.iloc[-1].name
            except:
                print (row.id_fine_wh)




                
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

            try:
                cursor.updateRow(row)
            except:
                print ("update error! ",row.id_fine_wh," ",year)


            

            if(int(round(count/10000))) == percent:
                print ("percent: %d%%" % (percent,))
                percent += 1

        print("yes")
