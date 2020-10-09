#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#######################################################################
# Author: Farid Wahabzada
# Support: Farid.Wahabzada1@gmail.com
########################################################################
# Dependencies: w_data (5).dat
# Inputs: w_data (5).dat
# Purpose: This programs purpose is to process the input file that it depends on, to be able to calculate the smallest temperature spread.
# Output: The day with the minimum spread in temperature based on the data present in the input file.
# Sample output: The Day with the minimum spread in temperature was Day: 14
########################################################################

WEATHER###############
infile = open('w_data (5).dat')
weather = {}
count = 0
for line in infile:
    list = line.split()
    if len(list) >= 5:
        weather[count] =[list[1],list[2]]
        count = count+1
minTempDay = 0
CurrMin = 1000
for Day, MaxMin in weather.items():
    if(Day > 0 ):
        if(  CurrMin > (int(MaxMin[0][0:2]) - int(MaxMin[1][0:2])) ):
            CurrMin = (int(MaxMin[0][0:2]) - int(MaxMin[1][0:2]))
            minTempDay = Day
print("Min")
print(minTempDay)
print(CurrMin)