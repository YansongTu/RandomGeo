# -*- coding: utf-8 -*-
"""
plate_div.py

Created on Wed Mar 13 10:34:54 2019

@author: Yansong Tu @ SUTPC

"""

import os

os.chdir("D:/Zhanjiang Traffic/Data/gpsData/bus/")
rootDir = os.getcwd()

plate_ref = None
plateholder = []

with open(rootDir + '/' + 'bus_plate_sorted.csv', 'r', encoding = 'UTF-8-Sig') as f:
    lines = f.readlines()
    for line in lines:
        if line.split(",")[0] == "plate_num":
            continue
        curr_plate = line.split(",")[0]
        if plate_ref == None:
            plate_ref = curr_plate
        elif curr_plate == plate_ref:
            plateholder = plateholder + [line]
        elif plate_ref != curr_plate:
            o_file = open(rootDir + '/' + plate_ref + '.txt', 'a', encoding = 'UTF-8-Sig')
            o_file.write("plate_num, timestamp, lat, lon\n")
            o_file.writelines(plateholder)
            o_file.close()
            plate_ref = curr_plate
            plateholder = []
                  