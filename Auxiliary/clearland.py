import os

if __name__ == '__main__':
     filedatas = []
 #    for year in range(2001,2002):
          for i in range(111):
               if i == 0:
                    continue
               elif i < 10:
                    file_data_ = u"Q:\\NEW(1)\\"+ str(year)+"\\Folder 0" + str(i)
               else:
                    file_data_ = u"Q:\\NEW(1)\\"+ str(year)+"\\Folder " + str(i)
               for j in range(400):
                    filedatas.append(file_data_ + "\\fragout" + str(j) + ".land")
                    
                    for k in range(1,11):
                         filedatas.append(file_data_ + "\\fragout" + str(j) + ".land_bk" + str(k))


     
     for filedata in filedatas:

          if os.path.isfile(filedata) == True:
                  os.remove(filedata)
     
