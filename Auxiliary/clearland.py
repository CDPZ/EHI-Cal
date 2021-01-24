import os

if __name__ == '__main__':
     filedatas = []
     for year in range(2002,2016):
          for i in range(4,110):
               if i == 0:
                    continue
               elif i < 10:
                    file_data_ = u"C:\\research\\NEW(1)\\"+ str(year)+"\\Folder 0" + str(i)
               else:
                    file_data_ = u"C:\\research\\NEW(1)\\"+ str(year)+"\\Folder " + str(i)
               for j in range(10):
                    filedatas.append(file_data_ + "\\fragout" + str(j) + ".land")
                    for k in range(1,11):
                         filedatas.append(file_data_ + "\\fragout" + str(j) + ".land_bk" + str(k))


     
     for filedata in filedatas:

          if os.path.isfile(filedata) == True:
                  os.remove(filedata)
     
