# -*- coding: utf-8 -*-
"""
file_sep.py

Created on Thu Mar 14 17:45:26 2019

@author: Yansong Tu @ SUTPC

- seperating files
- discarding old indexes and assign new ones

"""

import os
import math
import data_info as di

# EARTH_RADIUS

EARTH_RADIUS = 6378.137 #地球半径

# mutate plate number here (manually)

PLATE_NUM = "粤G93A30"

def checkTime(t1, t2, file):
    result = abs(int(t2) - int(t1))
    print(result)
    if result > di.time_eval(file):
        return True #filter out 
    else:
        return False

# checkDistance returns True when the distance between two logs 
#  is greater than the required difference in distance
# --- using radius query ---
def checkDistance(lat1, lng1, lat2, lng2, file):
    radLat1 = math.radians(lat1)
    radLat2 = math.radians(lat2)
    a = radLat1 - radLat2
    b = math.radians(lng1) - math.radians(lng2)
    
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a / 2), 2) + \
                               math.cos(radLat1) * math.cos(radLat2) * \
                               math.pow(math.sin(b / 2), 2)))
    s = s * EARTH_RADIUS
    s = round(s * 10000) / 10000
    print(s)
    if s >= di.dist_eval(file):
        return True # filter out
    else:
        return False

def file_seperation(): 
    os.chdir("C:/Users/admin/Desktop/test/")
    rootDir = os.getcwd()

### Hidden Markov Model

# evaluate the motionless feature

    f = open(rootDir + "/" + PLATE_NUM, 'r+', encoding = 'UTF-8-Sig')
# SORTED
    srt = sorted(f.readlines(), key=lambda line: int(line[1]))
    
    index = 1
    inner_i = 1
    lst = []

    curr_time = None
    curr_coor = []
    curr_line = None

    for line in srt:
        if line == curr_line:
            continue
        l_sep = line.split(",")    
    
        if curr_time == None or curr_coor == []:
            curr_time = l_sep[1]
            curr_coor = l_sep[2], l_sep[3]
            #latitude, longitude
            continue
       # variables: time; coordinates
        t1, t2 = curr_time, l_sep[1]
        lat1, lng1, lat2, lng2 = curr_coor[0], curr_coor[1], l_sep[2], l_sep[3]
        if checkTime(t1, t2) and checkDistance(float(lat1), float(lng1), float(lat2), float(lng2)): 
            lst.append(line)
            curr_f = open(PLATE_NUM + "_" + str(index) + ".txt", "w", encoding = "UTF-8-Sig")
            curr_f.write("plate_num, timestamp, lat, lon\n")
            curr_f.writelines(lst)
            curr_f.close()
            lst = []
            index += 1
        else: 
            lst.append(l_sep[0] + "," + l_sep[1] + "," + l_sep[2] + "," + \
                       l_sep[3] + ',' + inner_i)
        inner_i += 1
        curr_time = l_sep[1]
        curr_coor = [l_sep[2], l_sep[3]]
        print(curr_time, curr_coor[0], curr_coor[1])
