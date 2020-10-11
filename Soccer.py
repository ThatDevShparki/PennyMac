#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#######################################################################
# Author: Farid Wahabzada
# Support: Farid.Wahabzada1@gmail.com
########################################################################
# Dependencies: soccer.dat
# Inputs: soccer.dat
# Purpose: This programs purpose is to process the input file that it depends
# on, to be able to calculate the difference in 'For' and 'Against' points.
# Output: The team with the smallest difference in 'For' and 'Against' points
# based on the data present in the input file.
# Sample output: "Least difference in 'For' and 'Against' Team: Aston_Villa
# Assumptions made:   1) Currently the code is simple due to the file size
# being very small, but for a larger file and faster processing I would have
# used pandas.
#                     2) I am using absolute value in calcualting the 'For'
#                        and 'Against' points as the email mentioned " Write
#                        a program to print the name of the team with the
#                        smallest difference in ‘For’ and ‘Against’ goals."
#                     2.5) I could have chosen to not use absolute value but
#                          that would mean that the team would need a way
#                          larger against value and a much smaller for value
#                          and that would lead to negative numbers which doesnt
#                          really tell you the difference but rather how much
#                          point the other team made over yours.
########################################################################

# Read the input file
infile = open('soccer.dat')
# soccer is a dictionary that will hold all the score data in order to help
# compute.
soccer = {}
for line in infile:
    list = line.split()
    if len(list) >= 10:
        soccer[list[1]] = [list[6], list[8]]
# I keep track of which team has the lowest difference using empty string.
MinDiffTeam = ""
# Using CurrMin to keep track of the most minimum value after computing each
# line and teams scores in 'For' and 'Against.
CurrMin = 1000
# Getting the items from dictionary I made earlier but I am getting both the
# keys and values, as this the keys are team names and values are scores which
# are both needed.
for Team, ForAgainst in soccer.items():
    if(Team > 0):
        # non absolute value code START (If this code replaces line 58-59
        # then it would tell you how much the other team made over you.
        # Rather then the difference in score.)
        # if(CurrMin > abs(int(ForAgainst[1][0:2]) - int(ForAgainst[2][0:2]))):
        #      CurrMin = abs(int(ForAgainst[1][0:2]) - int(ForAgainst[2][0:2]))
        # non absolute value code END
        # Using absolute value to see the absolute difference between the two
        # points.
        if(CurrMin > abs(int(ForAgainst[0][0:2]) - int(ForAgainst[1][0:2]))):
            CurrMin = abs(int(ForAgainst[0][0:2]) - int(ForAgainst[1][0:2]))
            MinDiffTeam = Team
print("Least difference in 'For' and 'Against' Team: " + str(MinDiffTeam))
