# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 12:10:41 2019

@author: Yansong Tu @SUTPC

pseudocode ---------------- WARNING: DO NOT RUN THIS FILE ------------------

cmd for MapMatching: python bin/MapMatching.py data/StarTrek.txt data/StarTrek_gps.dat result/output.txt 

dictionary
    - yes: append 
    - no: create 

"""

import os
import json 

#from os.path import file, join
root_dir = "D:/Zhanjiang Traffic/Data/gpsData/bus"

# declaration dictionary_vehtype.txt?
# dictionary.txt - all the plates
# root folder - vehicle log 

# dictionary format:

#key + "," + values

# line[3]:line[0]+line[1],line[4],line[5],line[6],line[7]

dictionary = open(root_dir + "/" + "dictionary.txt", "w", encoding = "UTF-8")
for file in os.listdir(root_dir): 
    curr_file = open(file+"_mutated.txt", "w")
    curr_line = f.readline()
    if curr_line[3] in dictionary:
            curr_file = open(line[3] + ".txt", "w")
            curr_file.write(line[3] + "," + line[0] + line[1] + \
                            "," + line[4] + "," + line[5] + "," + line[6] + \
                            + "," + line[7] + "\n")
    new_file.writelines(dictionary)
    new_file.close()
            
''' Route 2 '''

dict_root_dir = "D:/Zhanjiang Traffic/Data/gpsData/bus/dicts"
for file in os.listdir(dict_root_dir):
    file.close()


''' -------- Plan II -------- '''

d = []
for file in os.listdir(root_dir):
    for line in file:
        curr_file = open(line[3] + ".txt", "w")
        new_line = [line[3] + "," + line[0] + line[1] + \
                        "," + line[4] + "," + line[5] + "," + line[6] + \
                        + "," + line[7]]
        dictionary.write(join(new_line) + "/n")
        ''' d.seek(0) '''
        curr_file.close()
    
''' -------- Plan III ------- ''' 

for file in os.listdir(root_dir): 
    curr_file = open(root_dir + "/" + file, "w", encoding = "UTF-8")
    print(file.name)
    lines = curr_file.readlines()
    for line in lines:
        if line[3] not in dictionary: #plate no.    
            new_line = [line[3] + "," + line[0] + line[1] + \
                            "," + line[4] + "," + line[5] + "," + line[6] + \
                            + "," + line[7]]
            dictionary.write(join(new_line) + "/n")
        elif line[3] in dictionary: #plate no.
            new_line = [line[3] + "," + line[0] + line[1] + \
                            "," + line[4] + "," + line[5] + "," + line[6] + \
                            + "," + line[7]]
            dictionary.write(join(new_line) + "/n")
            
dictionary.writelines()  
curr_file.close()
dictionary.close()

''' ------ Plan IV ------ '''

# read single file
# pseudocode

assign_num = 1
plate_dict = {}
output = []

for line in file:
    plate_num = line[3]
    if plate_num not in plate_dict:
        plate_dict['plate_num'] = assign_num
        output.extend(str(assign_num)+line[0]+line[1]+','+line[4]+','+line[5]+','+line[6]+','+line[7]+'\n')
        assign_num += 1
    elif plate_num in plate_dict:
        output.extend(str(assign_num)+line[0]+line[1]+','+line[4]+','+line[5]+','+line[6]+','+line[7]+'\n')
output.sort()
new_file = open(file)
new_file.writelines(output)
new_file.close()

for txtfile in platefolder:
    pass #apply 


''' --------- '''

# filename = file

# spectate a file and create dictionary logs of the vehicles and sort them
# if it is the first 

for line in file:   
    if line[3] in vehicle_dict:
        vehicle_dict[line[3]] + ['log' + str(len(vehicle_dict[line[3]) + 1), line[0], line[1], line[4], line[5]]]
    else:
        vehicle_dict[line[3]] = ['log1', line[0], line[1], line[4], line[5], line[6], line[7]]
        
for vehicle in vehicle_dict:
    vehicle_dict[vehicle] #.'export -> filename + type + vehicle.txt'
    
''' --------- '''

# read geoJSON files - attempt
x = 1
for coordinate in geoJSON.geometry:
    while next_coordinate != None:
        [coordinate, next_coordinate] = ID + "1"
        
''' --------- '''

def get_files_name(path):
    list_name = []
    for file in os.listdir(path):
        list_name.append(file)
        get_jobs_entity(path, list_name)
        
    for path in list_name:
        candidate = path.split()
        id1 = 0
        if 'json' not in candidate[0]:
            id1 = str(candidate[2])
        else:
            id1 = str(candidate[0])
        id1 = id1.split(".")[0]

''' --------- '''

# -*- coding:utf-8 -*- 
  
#os模块中包含很多操作文件和目录的函数 
import os 
#获取目标文件夹的路径 
meragefiledir = os.getcwd()+'\\MerageFiles'
#获取当前文件夹中的文件名称列表 
filenames = os.listdir(meragefiledir) 
#打开当前目录下的result.txt文件，如果没有则创建
file=open('result.txt','w') 
#向文件中写入字符 
  
#先遍历文件名 
for filename in filenames: 
  filepath=meragefiledir+'\\'
  filepath=filepath+filename
  #遍历单个文件，读取行数 
  for line in open(filepath): 
    file.writelines(line) 
  file.write('\n') 
#关闭文件 
file.close() 

''' open a file and read all lines '''

with open("data.txt", "r") as f:
    strings = f.readlines()
    
''' reading dat file '''

for line in open(filename, 'r'):
    item = line.rstrip() # strip off newline and any other trailing whitespace
    
''' sort txt file based on a given column of keys '''

for line in sorted(lines, key=lambda line: line.split()[0]):
    pass

''' sort txt file using csv module '''

import csv
from operator import itemgetter
reader = csv.reader(open('t.txt'), delimiter = '\t')

for line in sorted(reader, key = itemgetter(0)):
    print(line)
    
''' combine multiple files in one '''

''' Question: Why is there a memory leak in the following solution? '''

import os 

os.chdir("D:/Zhanjiang Traffic/Data/gpsData/taxi/")
rootDir = os.getcwd()

outfile = open('output.txt', 'w', encoding = 'UTF-8')

for fname in os.listdir(rootDir):
    if fname != 'output.txt':
        print(fname)
        infile = open(fname, 'r', encoding = 'UTF-8')
        curr_line = infile.readline()
        while curr_line != '':
            outfile.write(curr_line)
            curr_line = infile.readline()
    infile.close()
outfile.close()


''' GLOB 1 ''' 

import glob

read_files = glob.glob(".txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
            
''' GLOB 2 '''

from glob import iglob
import shutil
import os

path = r'C:\music'

destination = open('everything.mp3', 'wb')
for filename in iglob(os.path.join(PATH, '*.mp3')):
    shutil.copyfileobj(filename, 'rb'), destination)
destination.close()
            

''' LARGE '''

root_dir = "D:/Zhanjiang Traffic/Data/gpsData/bus"

with open('path/to/output/file', 'w') as outfile:
    for fname in os.listdir(root_dir):
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
 
               
''' SMALL '''

with open('path/to/output/file', 'w') as outfile:
    for fname in os.listdir(root_dir):
        with open(fname) as infile:
            outfile.write(infile.read())
            
''' Find and return the largest file in the directory '''

root = "demo"
root = os.path.abspath(root) 

def test(path):
    big_files = []
    all_paths = [x[0] for x in os.walk(path)]

    for paths in all_paths:

        f_list = filter(os.path.isfile, os.listdir(paths))
        if len(f_list) > 0:
            big_files.append((paths,max(f_list,key=os.path.getsize)))
    return big_files

print test(root)

''' timestamp to string '''

import datetime

datetime.datetime.

''''''

all_lines = f.readlines()
length = len(all_lines)
coor_dict = {}

# count_list

# 判断车辆在某个点的停滞性
count_list = []
max_occur = max(count_list)
if max_occur/length >= 0.5: # how do you actually determine this value?
    pass # discard the whole file
    
# 分开并写入到plate + index文件中

# line1, line2

# rootDir
for file in rootDir:
    plate = file.rstrip(".txt")

'''
# drop
for file in rootDir:
    #open
    length = len(file) 
    if length < 15:
        pathlib.Path.unlink(file)    
     
# coordinate references for occurences
coor_ref = []

# --- alternative 2 --- 
# assign new columns to ends of lines
index = 1

# file
for file in rootDir:
    f = open(rootDir + "/" + file, 'r', encoding = 'UTF-8-Sig')
    first_line = f.readline()
    log_sep = first_line.split(",")
    if coor_ref == []:
        continue
    else:
        coor_ref = [log_sep[3], log_sep[2]]

        
    # filter out those falling outside the link.txt
    # === read two logs at a time? ===
    # coordinates_first = firstlog[3], firstlog[2]
    # coordinates_second = secondlog[3], secondlog[2]
    # GetDistance()


gpsFilePath = "gps_wgs84.csv"
shapeFilePath = "shenzhen_osm_graph/shenzhen_osm_graph.shp"
tmpLocationPath = "/tmp/matching_example_location"

# <summary>
# 使用经纬度估算两点之间的距离（米）
# </summary>
# <param name="lat1"></param>
# <param name="lng1"></param>
# <param name="lat2"></param>
# <param name="lng2"></param>
# <returns></returns>

'''
# --- (manually?) filter out logs falling outside of the polygon
# filter out motionless logs
# --- evaluate mostly motionless logs

# if time is greater than ? minute(s)? 
# def checkTime():
    # pass
    # - filter out
    
# if distance is greater than 1km?
# def checkDistance():
    # pass
    # - filter out
        
# create individual log

# --- PSEUDOCODE ---

