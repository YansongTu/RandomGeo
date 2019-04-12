# -*- coding: utf-8 -*-
"""
geojson_txt.py

Created on Wed Mar 6 10:28:32 2019

@author: Yansong Tu @ SUTPC

"""

# 该文件可读取GeoJson文件中的特定信息及坐标, 并将其写出为txt或其他文本格式.

import json

linkshp = json.load(open('./linkjson.geojson', 'r', encoding = 'UTF-8'))
linkshp

linknet = []
for feature in linkshp['features']:
    coors = feature['geometry']['coordinates']
    for out_list in coors:
        for inner_list in out_list:
            for num in inner_list:
                coors_str = ''.join(str(num))
                linknet.append(float(coors_str))

seq = []
for feature in linkshp['features']:
    coor_list = feature['geometry']['coordinates'][0]
    concatenate = []
    for coor in coor_list: 
        coor = str(coor[0]) + ":" + str(coor[1]) + ";"
        concatenate.extend(coor)
    concatenated = "".join(concatenate)
    line = str(feature['properties']['LINKID']) + "," + str(feature['properties']['FROM_ID']) + "," + \
    str(feature['properties']['TO_ID']) + "," + str(feature['properties']['LENGTH']) + "," + \
    str(feature['properties']['TYPE']) + "," + concatenated
    length = len(line)
    seq.append(line[:length-1] + "\n")
    
file = open("link.txt", "w", encoding = 'UTF-8-Sig')
file.write("LinkID,FromNode,ToNode,Length,RoadClass,Geometry\n")
file.writelines(seq)
file.close()