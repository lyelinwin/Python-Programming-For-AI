# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:53:55 2024

@author: Lillian Nguyen
Title: Assignment 3
"""

# input
# Read Text File
with open('nba.txt', 'r') as file:
    file_content = file.readlines()
        
# dictionary to store info
#game is the parameter, acts as a placeholder for values that are passed to the function when called
def storing(games):
    counting_wins = {}
    for line in games:
        # splitting & slicing makes it easier and more direct with data
        split_list = line.split()
        section = split_list[0:4]
        # setting the index by double checking
        if len(section) < 4:
            # continue allows me to continue a for loop
            continue
    
        #assigning index to sections by extraction 
        # changing str into int of certain section
        team1 = section[0]
        score1 = int(section[1])
        team2 = section[2]
        score2 = int(section[3])
        
        # comparing scores 
        # the winner(team) is the key
        if score1 > score2:
            winner = team1
        else: 
            winner = team2
            
        # counting the number of wins each team has
        # the score of +=/=1 (number of wins) is the value
        if winner in counting_wins:
             counting_wins[winner] += 1
        else: 
            counting_wins[winner] = 1
    # return = statement used to end function and send result back to caller
    return counting_wins

# connecting file_content to storing function    
win_info = storing(file_content)

# output to the text file
#.items() used in to get list of key-value pairs 
with open ('wins.csv', 'w') as file:
    for team, number_wins in win_info.items():
        file.write(f'{team}, {number_wins}\n')
