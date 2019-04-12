# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:33:30 2019

@author: Yansong Tu @ SUTPC

"""

# 该文件将合并好的车辆按照车牌与时间进行排序，并将车牌替换成序号满足需要的格式。

import os

os.chdir("D:/Zhanjiang Traffic/Data/gpsData/coach/")
rootDir = os.getcwd()

assign_num = 1
plate_ref = {}
output = []

file = open(rootDir + '/' + 'coach_concat.txt', 'r', encoding = 'UTF-8-sig')

i = 1
line = file.readline()
while line != '':
    split_list = line.split(",")
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
    line = file.readline()
    plate_num = split_list[3]
    if plate_num not in plate_ref:
        plate_ref[plate_num] = assign_num
        output.append(str(assign_num)+','+split_list[0]+split_list[1]+','+split_list[4]+ \
                      ','+split_list[5]+','+split_list[6]+','+split_list[7] + '\n')
        assign_num += 1
        line = file.readline()
    elif plate_num in plate_ref:
        output.append(str(plate_ref[plate_num])+','+split_list[0]+split_list[1]+','+split_list[4]+\
                      ','+split_list[5]+','+split_list[6]+','+split_list[7] + '\n')
        line = file.readline()
        
#output = sorted(output, key = lambda x: int(x.strip().split(",")[0]))
new_file = open('truck_sorted_output.dat', 'w', encoding = 'UTF-8-sig')
new_file.writelines(output)
new_file.close()
