# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 17:16:24 2019

@author: Yansong Tu @ SUTPC

"""

import os 

outfile = open('test.txt', 'a', encoding = 'UTF-8-Sig')

os.chdir("D:/Zhanjiang Traffic/Data/gpsData/coach/")
rootDir = os.getcwd()

for fname in os.listdir(rootDir):
    if fname != 'coach_concat.txt' or fname != 'coach_sorted_output.dat':
        print(fname)
        infile = open(fname, 'r', encoding = 'UTF-8-Sig')
        curr_line = infile.readline()
        while curr_line != '':
            outfile.write(curr_line)
            curr_line = infile.readline()
    infile.close()
outfile.close()
