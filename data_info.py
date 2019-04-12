# -*- coding: utf-8 -*-
"""
data_info.py 

Created on Mon Mar 25 09:52:56 2019

@author: Yansong Tu @ SUTPC

"""

import os
import math
import statistics as st

# ===== CONSTANTS =====

#地球半径
EARTH_RADIUS = 6378.137

# 汽车种类 (手动修改)
CAR_TYPE = "taxi" 

# 有无进行过排序处理
SORTED = False

# get_time 获取单条记录的时间
def get_time(line):
    sep = line.split(",")[1]
    return sep


# get_coor 获取单条记录的坐标 (lon经度, lat纬度)
def get_coor(line):
    return [line.split(",")[3].rstrip("\n"), line.split(",")[2]]


# difference in time 获取两个timestamps的时间差
def TimeDiff(t1, t2): 
    return abs(int(t2) - int(t1))


# 通过时间判断两条记录之间是否为间隔可行的分割点
def checkTime(t1, t2, lines):
    result = abs(int(t2) - int(t1))
    if result > time_eval(lines):
        return True #filter out 
    else:
        return False


# difference in distances 获取两个坐标的距离差
def DistDiff(lat1, lng1, lat2, lng2):
    radLat1 = math.radians(float(lat1))
    radLat2 = math.radians(float(lat2))
    a = radLat1 - radLat2
    b = math.radians(float(lng1)) - math.radians(float(lng2))
    
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a / 2), 2) + \
                               math.cos(radLat1) * math.cos(radLat2) * \
                               math.pow(math.sin(b / 2), 2)))
    s = s * EARTH_RADIUS
    return round(s * 10000) / 10000


# 通过路程判断两条记录之间是否为间隔可行的分割点
def checkDistance(lat1, lng1, lat2, lng2, lines):
    radLat1 = math.radians(lat1)
    radLat2 = math.radians(lat2)
    a = radLat1 - radLat2
    b = math.radians(lng1) - math.radians(lng2)
    
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a / 2), 2) + \
                               math.cos(radLat1) * math.cos(radLat2) * \
                               math.pow(math.sin(b / 2), 2)))
    s = s * EARTH_RADIUS
    s = round(s * 10000) / 10000
    if s >= dist_eval(lines):
        return True # filter out
    else:
        return False
    
    
# count the number of files in a directory 获取单个文件夹内的文件数量
def file_count(rootDir):
    count = 0
    for file in rootDir:
        count += 1 
    return count


# total travel time 计算一辆车的行驶总时间
def totalTime(lines):
    time_traveled = 0
    index = 0
    curr_line = lines[index]
    while curr_line != '':
        if index == 0:
            index += 1
            curr_line = lines[index]
            try:
                curr_line = lines[index]
            except:
                break
        elif index == 1:
            prev_time = get_time(curr_line)
            index += 1
            try:
                curr_line = lines[index]
            except:
                break
        else:
            curr_time = get_time(curr_line)
            td = TimeDiff(curr_time, prev_time)
            time_traveled += td
            prev_time = curr_time
            index += 1
            try: 
                curr_line = lines[index]
            except:
                break
    return time_traveled

    
# total travel distance 计算一辆车的行驶总路程
def totalDistance(lines):
    dist_traveled = 0
    index = 0
    curr_line = lines[index]
    prev_coor = get_coor(lines[0])
    while curr_line != '':
        if index == 0:
            index += 1
            try:
                curr_line = lines[index]
            except:
                break
        elif index == 1:
            prev_coor = get_coor(curr_line)
            index += 1
            try:
                curr_line = lines[index]
            except:
                break
        else:
            curr_coor = get_coor(curr_line)
            dist = DistDiff(prev_coor[0], prev_coor[1], curr_coor[0], curr_coor[1])
            dist_traveled += dist
            prev_coor = curr_coor
            index += 1
            try: 
                curr_line = lines[index]
            except:
                break
    return dist_traveled


# create a list of time differences 生成时间差的list
def l_timeDiff(lines):
    length = len(lines)
    l = []
    prev_i = 1
    curr_i = 2
    try:
        prev_line = lines[prev_i]
        curr_line = lines[curr_i]
    except:
        return
    while curr_line != None and prev_line != None: 
        prev_line = lines[prev_i]
        curr_line = lines[curr_i]
        if isinstance(prev_line, int):
            break
        prev_time = get_time(prev_line)
        curr_time = get_time(curr_line)
        t = TimeDiff(prev_time, curr_time)
        l.append(float(t))
        prev_i += 1
        curr_i += 1
        if curr_i == length:
            break
    return l


# create a list of distance differences 生成距离差的list
def l_distDiff(lines):
    length = len(lines)
    l = []
    prev_i = 1
    curr_i = 2
    try:
        prev_line = lines(prev_i)
        curr_line = lines(curr_i)
    except:
        return
    while lines[prev_i] != None and lines[curr_i] != None:
        prev_line = lines[prev_i]
        curr_line = lines[curr_i]
        if isinstance(prev_line, int) or isinstance(prev_line, float):
            break
        prev_coor = get_coor(prev_line)
        curr_coor = get_coor(curr_line)
        d = DistDiff(prev_coor[1], prev_coor[0], curr_coor[1], prev_coor[0])
        l.append(float(d))
        prev_i += 1
        curr_i += 1
        if curr_i == length:
            break
        return l


# 该车拥有最长停车记录的坐标点 
def maxStoppedat(lines):
    # 生成停车记录参照表
    stop_dict = {}
    
    prev_coor = get_coor(lines[0])
    for line in lines:
        curr_coor = get_coor(lines[0])
        if prev_coor == curr_coor:
            if stop_dict:
                stop_dict[curr_coor[0] + "," + curr_coor[1]] += 1
            else:
                stop_dict[curr_coor[0] + "," + curr_coor[1]] = 2

    # 最长停车点(坐标)
    max_at = max(dict.values(stop_dict))
    for key in dict.keys(stop_dict):
        if stop_dict[key] == max_at:
            max_stopping_at = stop_dict[key]
            return max_stopping_at 


# 备注:
# 时间/距离差的计算方式
# stdv - standard deviation - 标准差
# 根据每一个数据的分布情况和波动大小来判断 - 具有独一性
# 平均值+标准差*0.9
            
# 计算分离文件的时间点
def time_eval(lines):  
    ltd = l_timeDiff(lines)
    stdv = st.pstdev(ltd)
    return (totalTime(lines)/(len(lines) - 1)) + stdv*0.9
 
    
# 计算分离文件的距离
def dist_eval(lines):
    lte = l_timeDiff(lines)
    stdv = st.pstdev(lte)
    return (totalTime(lines)/(len(lines) - 1)) + stdv*0.9
 
    
# 检查车辆全记录中的停车所占比
def stop_eval(lines):
    num = 0
    prev_coor = get_coor(lines[0])
    for line in lines:
        curr_coor = get_coor(line)
        if curr_coor == prev_coor:
            num += 1
        prev_coor = curr_coor
    actual_p = (num - 1)/len(lines)
    return actual_p


# 生成一个文件夹内的文件大小表
def file_sizes(rootDir):
    l = []
    for file in os.listdir(rootDir):
        size = os.path.getsize(file)
        l + [size]
    return l


# index: the index of the file 该车辆在全部同种类车辆的序号
# inner_i: the index of current line 车辆分割文件的序号

# 根据通过时间与距离上的正态分布检查   
def file_seperation(lines, plate_num, directory):
    srt = sorted(lines, key = lambda line:line.split(",")[1])
    
    index = 1
    inner_i = 1
    lst = []

    curr_time = None
    curr_coor = []
    curr_line = lines[0]
    
    # 创建新的文件夹以装载分割文件 (nfpath: new file path)
    nfpath = plate_num.rstrip(".txt") + "_sep"
    if not os.path.exists(nfpath):
        os.makedirs(nfpath)
    
    os.chdir(nfpath)

    for line in srt:
        if line == curr_line:
            continue
    
        l_sep = line.split(",") 
        
        if curr_time == None or curr_coor == []:
            curr_time = l_sep[1]
            curr_coor = l_sep[2], l_sep[3]
            continue
        
        t1, t2 = curr_time, l_sep[1]
        lat1, lng1, lat2, lng2 = curr_coor[0], curr_coor[1], l_sep[2], l_sep[3]
        if [lat1, lng1] == [lat2, lng2]:
            lst.append(line.rstrip("\n") + "," + str(index) + "\n")
            continue
        
        elif checkDistance(float(lat1), float(lng1), float(lat2), float(lng2), lines) or checkTime(t1, t2, lines): 
            lst.append(line.rstrip("\n") + "," + str(index) + "\n")
            curr_f = open(plate_num.rstrip(".txt") + "_" + str(index) + ".txt", "w", encoding = "UTF-8-Sig")
            curr_f.write("plate_num, timestamp, lat, lon\n")
            curr_f.writelines(lst)
            curr_f.close()
            lst = []
            index += 1
        else: 
            lst.append(l_sep[0] + "," + l_sep[1] + "," + l_sep[2] + "," + \
                       l_sep[3].rstrip("\n") + "," + str(index) + "\n")
        inner_i += 1
        curr_time = l_sep[1]
        curr_coor = [l_sep[2], l_sep[3]]      
        
        
# 分割后平均每条记录的样本分析
log_lst = []

def spcheck(plate, param, directory): 
    d = {}
    for file in os.listdir(directory):
        cf = open(file, mode = 'r', encoding = 'UTF-8-Sig')
        lines = cf.readlines()
        length = len(lines)
        d[file.rstrip(".txt")] = length - 1
        cf.close()
    
    #检查dictionary是否为空 - 如果是手动添加
    if d == {}:
        d = {plate + "_1": length}   
    if param == "files_sep":
        print("\n")
        print(d)
        # 分割后的文件总数
        files_sep = len(d)
        return files_sep
    elif param == "max_file_index":
        # 分割后拥有最多记录的文件索引
        maxcount = max(d.values()) 
        for key in d.keys():
            if d[key] == maxcount:
                return key.lstrip(plate + "_")
    elif param == "max_log_count":
        # 该文件所含有的记录数量
        max_log_count = max(d.values())
        return max_log_count
    elif param == "min_file_index":
        #分割后拥有最少记录的文件索引
        mincount = min(d.values())
        for key in d.keys():
            if d[key] == mincount:
                return key.lstrip(plate + "_")
    elif param == "min_log_count":
        # 该文件所含有的记录数量
        min_log_count = min(d.values())
        return min_log_count
    elif param == "avg_log_per_file":
        # === configure log_lst
        avg_log_per_file = sum(d.values())/length
        return avg_log_per_file
