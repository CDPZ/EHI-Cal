import os
path = "Q:\\out"
def gera_folder_path():
    paths = []
    for year in range(2002,2016):
        for i in range(111):  # 文件夹个数110
            if i == 0:
                continue
            elif i < 10:
                path = "Q:/out/"+str(year)+"/Folder 0" + str(i)
                paths.append(path)
            else:
                path = "Q:/out/"+str(year)+"/Folder " + str(i)    #E:/Cgrid_/
                paths.append(path)
    return paths

while(True):

        os.mkdir(path + "\\" + str(x) + "\\" + str(y))
        
