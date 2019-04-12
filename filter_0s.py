# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:33:30 2019

@author: Yansong Tu @ SUTPC

"""

import os
root_dir = "D:/Zhanjiang Traffic/Data/gpsData/taxi"

def filter_0s():
    for file in os.listdir(root_dir):
        print(file)
        f = open(root_dir + "/" + file, "r", encoding = "UTF-8")
        next_line = f.readline()
        out = open(file + ".txt", "w")
        coor_rec = []
        while next_line != "":
            print(next_line)
            curr = next_line.split(",")
            if curr[4] == 0 or curr[5] == 0:
                next_line = f.readline()
            else:
                coor_rec.append(str(curr[0])+","+str(curr[1])+","+str(curr[2])+","+ \
                str(curr[3])+","+str(curr[4])+","+str(curr[5])+","+ \
                str(curr[6])+","+str(curr[7])+","+str(curr[8])+","+ \
                str(curr[9])+"\n")
                
                next_line = f.readline()
        for line in coor_rec:
            out.write(line)
    f.close()
    out.close()
    