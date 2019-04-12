# -*- coding: utf-8 -*-
"""
dropdup_index.py

Created on Tue Mar 12 16:39:27 2019

@author: admin

"""

import os
import pandas as pd

os.chdir("D:/Zhanjiang Traffic/Data/gpsData/bus/")
rootDir = os.getcwd()

file = "bus_plate_sorted.csv"
data = pd.read_csv(os.path.join(rootDir, file), header = None, encoding = 'UTF-8', sep = ",")
data.columns = ['bus_no', 'timestamp', 'lat', 'lon']
data = data.drop_duplicates()

data.to_csv("bus_dupdroped.csv", index = False, header = False)
