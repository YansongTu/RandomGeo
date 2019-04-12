# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:02:34 2019

@author: Yansong Tu @ SUTPC

分析一个车辆种类的总体数据概况

"""

import os
import statistics as st
import data_info as di 

os.chdir("C:/Users/admin/Desktop/lilpys")
rootDir = os.getcwd()

TYPE = "bus"

ft = open(rootDir + "/" + TYPE + "/" + "plates_info.txt", "r", encoding = "UTF-8-Sig")

# create time list 
time_list = []
# create distance list
dist_list = []
# create time difference list 
l_timeDiff = []
# create a list of start times
l_start_t = []
# create a list of end times
l_end_t = []
# create distance difference list
l_distDiff = []
# create avg time_sep list
l_avg_timesep = []
# create avg dist_sep list
l_avg_distsep = []

ft.readline()
curr_line = ft.readline()
while curr_line != None:
    # start_time(timestamp)
    start_time = curr_line(",")[4]
    # end_time(timestamp)
    end_time = curr_line(",")[5]
    # time (timestamp)
    time = curr_line.split(",")[10]
    # dis (distance)
    dis = curr_line.split(",")[11]
    # td (time difference)
    td = curr_line.split(",")[12]
    # dd (distance difference)
    dd = curr_line.split(",")[13]
    # avgt (average time difference list)
    avgt = curr_line.split(",")[17]
    # avgd (average distance difference list)
    avgd = curr_line.split(",")[18]
    
    time_list = time_list + [time]
    dist_list = time_list + [dis]
    l_start_t = l_start_t + [start_time]
    l_end_t = l_end_t + [end_time]
    l_timeDiff = time_list + [td]
    l_distDiff = time_list + [dd]
    l_avg_timesep = time_list + [avgt]
    l_avg_distsep = time_list + [avgd]
    
    curr_line = ft.readline()

ft.write("车辆种类Vehicle Type: %s\n", TYPE)
ft.write("车辆总数Total Number of Vehicles: %d\n", di.file_count(ft))
ft.write("\n")

  # for line in file, append line.split(",")[10]
ft.write("平均行驶总时间 Average Total Travel Time: %d\n", st.mean(time_list, lambda x: int(x)))
ft.write("最长行驶总时间(+车牌) Minimum Total Travel Time: %d\n", min(time_list, lambda x: int(x)))
ft.write("最短行驶总时间(+车牌) Maximum Total Travel Time: %d\n", max(time_list, lambda x: int(x)))
ft.write("\n")

  # for line in file, append line.split(",")[11]
ft.write("平均行驶总路程 Average Total Travel Distance: %d\n", st.mean(dist_list, lambda x: int(x)))
ft.write("最长行驶总路程(+车牌) Minimum Total Travel Distance: %d\n", min(dist_list, lambda x: int(x)))
ft.write("最短行驶总路程(+车牌) Maximum Total Travel Distance: %d\n", max(dist_list, lambda x: int(x)))
ft.write("\n")

  # for line in file, append line.split(",")[4]
ft.write("平均记录开始时间 Average Log Start Time: %d\n", st.mean(di.s_t_mean(l_start_t)))
ft.write("最早记录开始时间(+车牌) Earliest Log Start Time: %d\n", min(di.s_t_mean(l_start_t)))
ft.write("最晚记录开始时间(+车牌) Latest Log Start Time: %d\n", max(di.s_t_mean(l_start_t)))
ft.write("\n") 

  # for line in file, append line.split(",")[5]
ft.write("平均记录结束时间 Average Log End Time: %d\n", st.mean(di.e_t_mean(l_end_t)))
ft.write("最早记录结束时间(+车牌) Earliest Log End Time: %d\n", min(di.e_t_mean(l_end_t)))
ft.write("最晚记录结束时间(+车牌) Latest Log End Time: %d\n", max(di.e_t_mean(l_end_t)))
ft.write("\n") 

  # for line in file, append line.split(",")[12]
ft.write("平均时间间隔 Average Total Time Difference: %d\n", st.mean(l_timeDiff, lambda x: int(x)))
ft.write("最长时间间隔[除0外](+车牌) Minimum Total Time Difference: %d\n", min(l_timeDiff, lambda x: int(x)))
ft.write("最短时间间隔(+车牌) Maximum Total Time Difference: %d\n", max(l_timeDiff, lambda x: int(x)))
ft.write("\n") 

  # for line in file, append line.split(",")[13]
ft.write("平均距离间隔 Average Total Distance Difference: %d\n", st.mean(l_distDiff, lambda x: int(x)))
ft.write("最小距离间隔[除0外](+车牌) Minimum Total Distance Difference: %d\n", min(l_distDiff, lambda x: int(x)))
ft.write("最大距离间隔(+车牌) Maximum Total Distance Difference: %d\n", max(l_distDiff, lambda x: int(x)))
ft.write("\n")

  # for line in file, append line.split(",")[17]
ft.write("平均文件切分时间间隔 Average Time Seperation Point: %d\n", st.mean(l_avg_timesep, lambda x: int(x)))
ft.write("最小文件切分时间间隔(+车牌) Minimum Time Seperation Point: %d\n", min(l_avg_timesep, lambda x: int(x)))
ft.write("最大文件切分时间间隔(+车牌) Maximum Time Seperation Point: %d\n", max(l_avg_timesep, lambda x: int(x)))
ft.write("\n")

  # for line in file, append line.split(",")[18]
ft.write("平均文件切分距离间隔 Average Distance Seperation Point: %d\n", st.mean(l_avg_distsep, lambda x: int(x)))
ft.write("最短文件切分距离间隔(+车牌) Minimum Distance Seperation Point: %d\n", min(l_avg_distsep, lambda x: int(x)))
ft.write("最长文件切分距离间隔(+车牌) Maximum Distance Seperation Point: %d\n", max(l_avg_distsep, lambda x: int(x)))
ft.write("\n")

ft.close()