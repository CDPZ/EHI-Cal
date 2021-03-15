import os

if __name__ == '__main__':

    for i in range(8):
        path = "F:\\sub\\Folder 11" + str(i + 1)
        for root, dirs, files in os.walk(path):
            for f in files:
                os.rename(path + "\\" + f, path + "\\id_fine_wh_" + f)
                
