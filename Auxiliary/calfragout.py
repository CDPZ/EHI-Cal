import os 

if __name__ == '__main__':

    for i in range(6,111):
        for j in range(200):
            if i < 10:
                file_data = u"Q:\\NEW(1)\\2002\\Folder 0" + str(i) + "\\fragout"+str(j)+".land"
            else:
                file_data = u"Q:\\NEW(1)\\2002\\Folder " + str(i) + "\\fragout"+str(j)+".land"
            if os.path.isfile(file_data) == True:
                os.remove(file_data)
