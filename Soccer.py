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

# Soccer###############
infile = open('soccer.dat')
soccer = {}
count = 0
for line in infile:
    list = line.split()
    if len(list) >= 10:
        soccer[count] =[list[1], list[6],list[8]]
        count = count+1
MinDiffTeam = ""
CurrMin = 1000
for Team, ForAgainst in soccer.items():
    if(Team > 0 ):
        if(  CurrMin > (int(ForAgainst[1][0:2]) - int(ForAgainst[2][0:2])) ):
            CurrMin = (int(ForAgainst[1][0:2]) - int(ForAgainst[2][0:2]))
            MinDiffTeam = ForAgainst[0]
print("Min")
print(MinDiffTeam)
print(CurrMin)