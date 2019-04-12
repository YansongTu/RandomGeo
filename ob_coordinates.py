import os
root_dir = "E:/Zhanjiang Traffic/Data/gpsData/bus"

def ob_coordinates():
    for file in os.listdir(root_dir):
        filename = file
        f = open(root_dir + "/" + filename, "r", encoding = 'UTF-8')
        next_line = f.readline()
        out = open(filename + "coor.txt", "w")
        coor_rec = []
        while next_line != "":
            curr = next_line.split(",")
            if curr[4] == 0 or curr[5] == 0:
                next_line = f.readline()
            else:
                coor_rec.append(str(curr[4]) + "," + str(curr[5]) +"\n")
                next_line = f.readline()
        for item in coor_rec:
            out.write(item)
    f.close()
    out.close()
        