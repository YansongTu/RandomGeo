# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:04:08 2019

@author: Yansong Tu @ SUTPC

分析一个车辆种类内每个文件(每一辆)的数据概况
    
"""
import os
import data_info as di

# plate number defined here is for testment only

os.chdir("D:/Zhanjiang Traffic/Data/GpsData/truck/truck_plate_div")
rootDir = os.getcwd()

#车辆种类 (手动修改)
TYPE = "truck"

f = open(rootDir + "/" + TYPE + "_plates_info.txt", 'w', encoding = 'UTF-8-Sig')    
f.write("plate,type,log_num,file_size,start_time,end_time,start_coor_lon,start_coor_lat,end_coor_lon,end_coor_lat,totaL_travel_time,total_travel_distance,avg_time_diff,avg_dist_diff,is_stopping,is_half_stopping,max_stopping_at,sep_at_time,sep_at_dist,files_sep,max_file_index,max_log_count,min_file_index,min_log_count,avg_log_per_file\n")

to_write = [] 

index = 1

for file in os.listdir(rootDir):
    if file != TYPE + "_plates_info.txt" and file != "data_info.py" and os.path.isfile(file):
        print("\n")
        print(str(index) + ": ========== " + file.rstrip(".txt") + " ==========")
        cf = open(rootDir + "/" + file, 'r', encoding = 'UTF-8-Sig')
        lines = cf.readlines()
        sl = sorted(lines, key = lambda line:line.split(",")[1])
        cf.close()
        first_line = sl[1]
        last_line = sl[-1]
       
        # 车牌
        plate = file.rstrip(".txt")
        
        # 检查是否85%及以上的记录处于停车状态
        # (如果某车超过85%的记录处于停车状态,则判定为不合格记录,筛除)
        se_result = di.stop_eval(sl)
        print(se_result)
        is_stopping = se_result > 0.85
        files_dropped = 0
        if is_stopping:
            #os.remove(file)
            files_dropped += 1
            print(file + " has been dropped")
            to_write.extend(plate + ",Dropped due to Stopping Percentage > 90% \n")
            index += 1
            continue
            
        else:   
            # 车辆总类
            # 注：TYPE已经在上方define过
            # 记录总数 - CHECK
            log_num = len(sl) - 1
            # 文件大小 - CHECK
            file_size = os.path.getsize(file)
            # 起始时间 - CHECK
            start_time = di.get_time(first_line)
            # 终止时间 - CHECK
            end_time = di.get_time(last_line)
            # 起始坐标 - 经度 (lon)
            start_coor_lon = di.get_coor(first_line)[0]
            # 起始坐标 - 纬度 (lat)
            start_coor_lat = di.get_coor(first_line)[1]
            # 终止坐标 - 经度 (lon)
            end_coor_lon = di.get_coor(last_line)[0]
            # 终止坐标 - 纬度 (lat)
            end_coor_lat = di.get_coor(last_line)[1]
            # 行驶总时间
            total_travel_time = di.totalTime(sl)
            # 行驶总路程
            total_travel_distance = di.totalDistance(sl)
            # 平均时间间隔
            avg_time_diff = di.totalTime(sl)/(log_num - 1)
            # 平均距离间隔
            avg_dist_diff = di.totalDistance(sl)/(log_num - 1)
            # 检查是否50%及以上的记录处于停车状态(准不合格记录,运行算法时不予优先考虑)
            is_half_stopping = di.stop_eval(sl) > 0.5
            # 该车拥有最长停车记录的坐标点        
            max_stopping_at = di.maxStoppedat(sl)
            # 时间分割点
            sep_at_time = di.time_eval(sl)
            # 距离分割点
            sep_at_dist = di.dist_eval(sl)      
            # ========== 分割文件 ========== 
            di.file_seperation(sl, file, rootDir)        
            # 分割后的文件总数
            files_sep = di.spcheck(plate, "files_sep", rootDir + "/" + plate + "_sep")
            # 分割后拥有最多记录的文件索引
            max_file_index = di.spcheck(plate, "max_file_index", rootDir + "/" + plate + "_sep")
            # 该文件所含有的记录数量
            max_log_count = di.spcheck(plate, "max_log_count", rootDir + "/" + plate + "_sep")
            # 分割后拥有最少记录的文件索引
            min_file_index = di.spcheck(plate, "min_file_index", rootDir + "/" + plate + "_sep")
            # 该文件所含有的记录数量
            min_log_count = di.spcheck(plate, "min_log_count", rootDir + "/" + plate + "_sep")
            # === configure log_lst
            avg_log_per_file = di.spcheck(plate, "avg_log_per_file", rootDir + "/" + plate + "_sep")
            
            os.chdir(rootDir)
            # 被削除的文件数量 
            # files_dropped
            
            new_write_l = [plate + "," + TYPE + "," + str(log_num) + "," + str(file_size) + "," + str(start_time) + "," + \
                           str(end_time) + "," + str(start_coor_lon) + "," + str(start_coor_lat) + "," + str(end_coor_lon) + "," + \
                           str(end_coor_lat) + "," + str(total_travel_time) + "," + str(total_travel_distance) + "," + \
                           str(avg_time_diff) + "," + str(avg_dist_diff) + "," + str(int(is_stopping)) + "," + str(int(is_half_stopping)) + "," + \
                           str(max_stopping_at) + "," + str(sep_at_time) + "," + str(sep_at_dist) + "," + str(files_sep) + "," + str(max_file_index) + \
                           "," + str(max_log_count) + "," + str(min_file_index) + "," + str(min_log_count) + "," + str(avg_log_per_file) + "\n"]
            
            print("\n")
            print(new_write_l)
            to_write.extend(new_write_l)
        
        index += 1

f.writelines(to_write)
f.close()
print("Mission Accomplished. Dropped %d files", files_dropped)
