# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:33:30 2019

@author: Yansong Tu @ SUTPC

"""

# 该文件将合并好的车辆按照车牌与时间进行排序，并整理车辆。

import os 
import time
import datetime
import codecs

def string2timestamp(strValue):
    try:        
        d = datetime.datetime.strptime(strValue, "%Y-%m-%d %H:%M:%S.f")
        t = d.timetuple()
        timeStamp = int(time.mktime(t))
        timeStamp = float(str(timeStamp) + str("%06d" % d.microsecond))/1000000
        print(timeStamp)
        return timeStamp
    except ValueError as e:
        print(e)
        d = datetime.datetime.strptime(strValue, "%Y-%m-%d %H:%M:%S")
        t = d.timetuple()
        timeStamp = int(time.mktime(t))
        timeStamp = float(str(timeStamp) + str("%06d" % d.microsecond))/1000000
        print(timeStamp)
        return timeStamp

        
os.chdir("D:/Zhanjiang Traffic/Data/gpsData/coach/")
rootDir = os.getcwd()

output = []

file = open(rootDir + '/' + 'coach_concat.txt', 'r', encoding = 'UTF-8-Sig')

line = file.readline()
while line != '':
    split_list = line.split(",")
    # 检查length
    length = len(split_list[1])
    if length == 1:
        split_list[1] = '00000' + split_list[1]
    if length == 2:
        split_list[1] = '0000' + split_list[1]
    if length == 3:
        split_list[1] = '000' + split_list[1] 
    if length == 4:
        split_list[1] = '00' + split_list[1]
    if length == 5:
        split_list[1] = '0' + split_list[1]
    date = split_list[0]
    if date[0] == codecs.BOM_UTF8:
        date = date.strip("\ufeff")
    time_sec = split_list[1]
    mdate = date[0:4] + "-" + date[4:6] + "-" + date[6:8]
    mtime_sec = time_sec[0:2] + ":" + time_sec[2:4] + ":" + time_sec[4:6]
    date_time = mdate + " " + mtime_sec
    # time -> directly to timestamp
    tstamp = string2timestamp(date_time)
    line = file.readline()
    plate = str(split_list[3])
    # plate + time stamp + latitude + longitude
    output.append(str(plate) + "," + str(tstamp) + "," + \
                  str(split_list[5]) + "," + \
                  str(split_list[4]) + "\n") 
    line = file.readline()
     
# output = sorted(output, key = lambda x: int(x.strip().split(",")[0]))
# drop duplicates? - manually
    
new_file = open('coach_plate_sorted.csv', 'w', encoding = 'UTF-8-Sig')
new_file.write("coach_no, timestamp, lat, lon\n")
new_file.writelines(output)
new_file.close()
file.close()
