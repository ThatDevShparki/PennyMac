#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#######################################################################
# Author: Farid Wahabzada
# Support: Farid.Wahabzada1@gmail.com
########################################################################
# Dependencies: soccer.dat
# Inputs: soccer.dat
# Purpose: This programs purpose is to process the input file that it depends on, to be able to calculate the diffrance in 'for' and 'against' points
# Output: The team with the smallest diffrance in 'for' and 'Against' points based on the data present in the input file.
# Sample output: The team with the smallest diffrance in 'for' and 'against' points is: 
# Assumptions made:   1) Currently the code is simple due to the file size being very small, but for a larger file and faster processing I would have used pandas
#                     2) I am using absolute value in calcualting the 'for' and 'Against' points as the email mentioned " Write a program to print the name of the team with the smallest difference in ‘for’ and ‘against’ goals."
#                     2.5) I could have chosen to not use absolute value but that would mean that the team would need a way larger against value and a much smaller for value and that would lead to negative numbers which doesnt really tell you the diffrance but rather how much point the other team made over yours. 
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
    	# non absolute value code START ( this code if enabled with the other two disabled, would tell you how much the other team made over you. Rather then the differance in score)
    	# if(  CurrMin > abs(int(ForAgainst[1][0:2]) - int(ForAgainst[2][0:2])) ):
     #        CurrMin = abs(int(ForAgainst[1][0:2]) - int(ForAgainst[2][0:2]))
        #non absolute value code END
        # Using absolute value to see the absolute differance between the two points 
        if(  CurrMin > abs(int(ForAgainst[1][0:2]) - int(ForAgainst[2][0:2])) ):
            CurrMin = abs(int(ForAgainst[1][0:2]) - int(ForAgainst[2][0:2]))
            MinDiffTeam = ForAgainst[0]
print("The team with the smallest diffrance in 'for' and 'against' points is:" + str(MinDiffTeam))
