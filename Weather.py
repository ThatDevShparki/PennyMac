#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#######################################################################
# Author: Farid Wahabzada
# Support: Farid.Wahabzada1@gmail.com
########################################################################
# Dependencies: w_data (5).dat
# Inputs: w_data (5).dat
# Purpose: This programs purpose is to process the input file that it depends
# on, to be able to calculate the smallest temperature spread.
# Output: The day with the minimum spread in temperature based on the data
# present in the input file.
# Sample output: The day with minimum spread in temperature, Day: 14
# Assumptions made:  Currently the code is simple due to the file size being
# very small, but for a larger file and faster processing I would have used
# pandas.
########################################################################
# weather is a dictionary that will hold all the temperature data in order to
# help compute.
weather = {}
count = 0
# Read the input file
with open('w_data (5).dat') as infile:
    # Process the file and parse the data within to get data we need to
    # calculate minimum temperature spread.
    for line in infile:
        list = line.split()
        # read lines that are not empty and contain data I need to compute.
        if len(list) >= 5:
            weather[count] = [list[1], list[2]]
            count = count+1
# Use the data processed to find the current minimum temperature spread.
# Keep track of the day with minimum temperature with minTempDay.
minTempDay = 0
# Keep track of current minimum with CurrMin.
CurrMin = 1000
for Day, MaxMin in weather.items():
    if(Day > 0):
        # check to see if I have most minimum data stored before storing it.
        if(CurrMin > (int(MaxMin[0][0:2]) - int(MaxMin[1][0:2]))):
            CurrMin = (int(MaxMin[0][0:2]) - int(MaxMin[1][0:2]))
            minTempDay = Day
print("The day with minimum spread in temperature, Day: " + str(minTempDay))
