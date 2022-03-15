import arcpy
import pandas as pd
#
#linked = "D:/DaTa/Yangtz/workflow/shape_ehi/fishnet/1km_inter.shp"

#the path of the shps to be linked. The shps themself need to originate from the split and intersected fishnet of the research zone by importing into the data base and create float fields in the name of indexs. Make sure the shps' name are the years they would later represent.需基于打散并相切的渔网shp导入数据库后添加float类型各指标字段并于复制粘贴后各自命名为对应年份
shppath = "E:/final/out/SHP/years.mdb/"
#the path of the tables to be linked. The tables ought to be the result of mergetable and gelid process, the names of them should be like %year%fkj.csv链接表的目录，文件应经过mergetable，gelid处理，名字应符合
csvpath = "E:/final/out/CSV/"
#count for the record processed in this run, it was meant to indicate the progress rate.
count = 0
#count for the record processed of the shp, it was meant to indicate the progress rate.
percent = 0

#set null of a certain year's shp
def setna(year, metrics):                                                   #metrics (list obj) contain all the indexs involved.like["PAFRAC", "IJI", "DIVISION", "CONTAG", "SHEI", "SHDI"]
    cursor = arcpy.UpdateCursor(shppath + "b" + str(year))                  #the row from the cursor will act as the iterator to handle each row of records.
    print ("setnull...")
    for row in cursor:
        for metric in metrics:
            try:
                row.setNull(metric)                                         #A methord from arcpy
            except:
                print ("update_" + metric + " error! ",row.idj," ",year)
        cursor.updateRow(row)                                               #like it++ in C++
    del cursor, row

#link
def setdata(The_Line, The_Index, row, metric):                              #The_Line (series obj) is the record with the specific idj; The_Index (index obj) is the index of The_Line; Metric (str obj) is an index
    try:
        index = The_Line.loc[The_Index, ' ' + metric]                       #obtain index value from the record
        if not isinstance(index, str):                                      #Check the property of the index in the record. "DIVISION" index is often recognize by pandas as float, however others often string. 
            if isinstance(index,float):
                index = str(round(index, 4))                                #if it is float, then transform it into "x.yyyy"
            else:
                print("Unexpected index type!")
        if index.strip(' ') != "N/A":                                       #the null record in arcgis ought to be like " N/A ", for safty's sake, we use strip() to erase the potential blank in the variable index
            #print("ok")
            row.setValue(metric, float(index))                              #A methord from arcpy
    except:
        print(metric + " can't be updated!")
        print(row.idj)
        
if __name__ == '__main__':
    metrics = ["PAFRAC", "IJI", "DIVISION", "CONTAG", "SHEI", "SHDI"]       #The metrics to be processed
    for year in [2000,2010,2020]:                                           
        print (year)
        setna (year, metrics)                                               #This sentence is essential when the shps are linked for the first time. But if you have run this script before, you may comment this line for it to proceed on old works
        data = pd.read_csv(csvpath + str(year) + "fkj.csv")
        #data.sort_values("LID", inplace=True)
        cursor = arcpy.UpdateCursor(shppath + str(year))                    #the row from the cursor will act as the iterator to handle each row of records.
        print ("start...")
        
        for row in cursor:
            if row.IJI == None or row.PAFRAC == None or row.SHEI == None or row.SHDI == None or row.CONTAG == None or row.DIVISION == None:
                The_Line = data[data.LID == int(row.idj)]                   #extract The_Line (series obj) which is the record with the specific idj
                try:
                    The_Index = The_Line.iloc[-1].name                      #The_Index (index obj) is the index of The_Line
                    for metric in metrics:
                        setdata(The_Line, The_Index, row, metric)
                except:
                    print("can't located the LID")
                    print (row.idj)

                count += 1
            else:
                continue
            try:
                cursor.updateRow(row)
            except:
                print ("update error! ",row.idj," ",year)

            if(int(round(count/10000))) == percent:
                print ("percent: %d%%" % (percent,))
                percent += 1
        

        print("yes")
