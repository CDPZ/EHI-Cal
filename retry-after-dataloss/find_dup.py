import os

path = "D:\\research\\subwhsp"


def walkFile(file):
    IDs = []
    ID_dup = []
    print("start_2_sta")
    for root, dirs, files in os.walk(file):
        for f in files:
            # print(os.path.join(root, f))
            (filename, extension) = os.path.splitext(f)
            if extension == ".shp":
                if filename not in IDs:
                    IDs.append(filename)
                else:
                    ID_dup.append(filename)

    return ID_dup
def save_2_csv(save_path, ITEMS):
    
    with open(save_path, 'w') as f:
        for ITEM in ITEMS:
            f.write(ITEM)
            f.write('\n')
def main():
    IDs = walkFile(path)
    print("start_2_write")
    save_2_csv("F:\sta_sub\dup.csv", IDs)
if __name__ == '__main__':
    main()