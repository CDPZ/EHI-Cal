# -*- coding: utf-8 -*-

import os

def walkFile(file):
    IDs = []
    print("start_2_sta")
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件

        for f in files:
            # print(os.path.join(root, f))
            (filename, extension) = os.path.splitext(f)
            if filename  not in IDs:
                IDs.append(filename)

        # 遍历所有的文件夹

        # for d in dirs:
        #     print(os.path.join(root, d))
    return IDs
def save_2_csv(save_path, ITEMS):
    
    with open(save_path, 'w') as f:
        for ITEM in ITEMS:
            f.write(ITEM)
            f.write('\n')
def main():
    IDs = walkFile("F:\\sub")
    print("start_2_write")
    save_2_csv("F:\sta_sub\sta.csv", IDs)

if __name__ == '__main__':
    main()
