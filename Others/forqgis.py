import os
import shutil
import win32file
import time

def is_used(file_name):
	try:
		vHandle = win32file.CreateFile(file_name, win32file.GENERIC_READ, 0, None, win32file.OPEN_EXISTING, win32file.FILE_ATTRIBUTE_NORMAL, None)
		return int(vHandle) == win32file.INVALID_HANDLE_VALUE
	except:
		return True
	finally:
		try:
			win32file.CloseHandle(vHandle)
		except:
			pass

def take_out(name, extensions):
    pack = []
    for extension in extensions:
        pack.append(name + extension)
    return pack


def walk(path):
    while True:
        ff = os.walk(path)
        time = 0
        extensions = []
        check = 0
        packs = []
        for root, dirs, files in ff:
            for file in files:
                (filename, extension) = os.path.splitext(file)
                if time == 0:
                    time += 1
                    extensions.append(extension)
                    last = filename
                    continue
                elif list(filename) == list(last):
                    time += 1
                    extensions.append(extension)
                    continue
                elif time == 4:
                    packs.append(take_out(last, extensions))
                    time = 1
                    extensions[:] = []
                    last = filename
                    extensions.append(extension)
                    return packs
                elif time < 4:
                    return None
                    # check = 1
                    # packs.append(take_out(last, extensions))
                    # time = 1
                    # extensions[:] = []
                    # last = filename
                    # extensions.append(extension)
                    # continue
                else:
                    print("time = ")
                    print(time)
                    print("logic missed.")
                    os.system("pause")
                if check == 1:
                    break
            if time == 4:
                packs.append(take_out(last, extensions))
                time = 1
                extensions[:] = []
                last = filename
                extensions.append(extension)
                return packs
            elif time < 4:
                return None
                # check = 1
                # packs.append(take_out(last, extensions))
                # time = 1
                # extensions[:] = []
                # last = filename
                # extensions.append(extension)
                # continue
            else:
                print("time = ")
                print(time)
                print("logic missed.")
                os.system("pause")
            if check == 1:
                break
# =============================================================================
# def through_walk():
#     des = "D:/AAAAAAAAAA/3KMSave"
#     for 
#     for listx in os.listdir(des + )
#                     
# =============================================================================

if __name__ == '__main__':
    ger_path = "E:/AAAAAAAAAA/3KMout"
    des = "D:/AAAAAAAAAA/3KMSave"
    des_path = "D:/AAAAAAAAAA/3KMSave"
    i = 0
    cou_fld = 0

    while i == 0:
        packs = walk(ger_path)
        if packs is not None:
            cou_fld += 1
            if cou_fld < 100000:
                fine = ''.join(des)
                des_path = "D:/AAAAAAAAAA/3KMSave/Folder 0" + str(int(cou_fld/10000) + 1)
                if not os.path.isdir(fine + "/Folder 0" + str(int(cou_fld/10000) + 1)):
                    os.mkdir(des_path)
            else:
                fine = ''.join(des)
                des_path = "D:/AAAAAAAAAA/3KMSave/Folder " + str(int(cou_fld/10000) + 1)
                if not os.path.isdir(fine + "/Folder " + str(int(cou_fld/10000) + 1)):
                    os.mkdir(des_path)
            for pack in packs:
                for file in pack:
                    if not is_used(ger_path + '/' + file):
                        shutil.move(ger_path + '/' + file, des_path + '/')
                    else:
                        time.sleep(0.5)
                        if is_used(ger_path + '/' + file):
                            time.sleep(1)
                            if is_used(ger_path + '/' + file):
                                time.sleep(1)
                                if is_used(ger_path + '/' + file):
                                    print("thing bad")
                                else:
                                    shutil.move(ger_path + '/' + file, des_path + '/')
                            else:
                                shutil.move(ger_path + '/' + file, des_path + '/')
                        else:
                            shutil.move(ger_path + '/' + file, des_path + '/')
