# -*- coding: utf-8 -*-
"""

PlateSepEvaluation.py

Created on Mon Apr 8 09:59:59 2019

@author: Yansong Tu @ SUTPC
"""

import os
import data_info as di

# ========== 分割文件 ========== 

TYPE = "bus"

# mutated manually
PLATE_NUM = "粤GYD730"
os.chdir("C:/Users/admin/Desktop/test/")
rootDir = os.getcwd()
   
tw = "plate,type,log_num,file_size,start_time,end_time,start_coor_lon,start_coor_lat,end_coor_lon,end_coor_lat,total_travel_time,total_travel_distance,avg_time_diff,avg_dist_diff,is_stopping,is_half_stopping,max_stopping_at,sep_at_time,sep_at_dist,plate,type,log_num,file_size,start_time,end_time,start_coor_lon,start_coor_lat,end_coor_lon,end_coor_lat,total_travel_time,total_travel_distance,avg_time_diff,avg_dist_diff,is_stopping,is_half_stopping,max_stopping_at,sep_at_time,sep_at_dist,files_sep,max_file_sep_index,max_log_count,min_file_sep,min_log_count,avg_log_per_file\n"

to_write = []
to_write.extend(tw)

# 分割后的文件总数
files_sep = di.spcheck("files_sep")
# 分割后拥有最多记录的文件索引
max_file_index = di.spcheck("max_file_index")
# 该文件所含有的记录数量
max_log_count = di.spcheck("max_log_count")
# 分割后拥有最少记录的文件索引
min_file_index = di.spcheck("min_file_index")
# 该文件所含有的记录数量
min_log_count = di.spcheck("min_log_count")
# === configure log_lst
avg_log_per_file = di.spcheck("avg_log_per_file")
# 被削除的文件数量 
#files_dropped

to_write.extend([str(files_sep) + "," + str(max_file_index) + "," + str(max_log_count) + "," + \
                 str(min_file_index) + "," + str(min_log_count) + "," + str(avg_log_per_file) + "\n"])

prevf = open(TYPE + '_plates_info', mode = 'r', encoding = 'UTF-8-Sig')
currf = open(mode = 'r', encoding = 'UTF-8-Sig')

plines = prevf.readlines()
clines = currf.readlines()

concat = open("full_data_info.txt", mode = 'w', encoding = 'UTF-8-Sig')
index = 0
prev_line = plines[index]
curr_line = clines[index + 1]
while prev_line != '' and curr_line != '':
      new_line = prev_line + ',' + curr_line
      tw.extend(new_line)
      index += 1
      try:
          prev_line = plines[index]
          curr_line = clines[index + 1]
      except:
         break

concat.writelines(tw)
concat.close()

#file concatenation
a = open("full_plate", )
al = a.readlines()
a.writeline()
a.close()
print("Accomplished")


