import os 

if __name__ == '__main__':

    for i in range(111):
        for j in range(400):
            if i < 10:
                file_data = u"Q:\\NEW(1)\\2003\\Folder 0" + str(i) + "\\fragout"+str(j)+".land"
            else:
                file_data = u"Q:\\NEW(1)\\2003\\Folder " + str(i) + "\\fragout"+str(j)+".land"
            if os.path.isfile(file_data) == True:
                os.remove(file_data)
