# Python Data Analysis - Mike Fortin
import numpy as np
import pandas as pd
import csv

def decimal_to_percentage(decimal):
    percentage = decimal * 100
    percentage = round(percentage, 1)
    return percentage

data_path = "/Users/Mike/Desktop/ufc-analysis/data.csv"

data = pd.read_csv(data_path)
red_or_blue = data.Winner
#print(red_or_blue)

total_fights = len(red_or_blue)
#print(total_fights)
red_wins = 0

for fight in red_or_blue:
    #print(fight)
    if fight == "Red":
        red_wins += 1
#print(red_wins)
red_win_pct = decimal_to_percentage(float(red_wins) / total_fights)

red_height = data.R_Height_cms
blue_height = data.B_Height_cms

taller_fighter_wins = 0

for i in range(0,total_fights):
    if red_height[i] > blue_height[i] and red_or_blue[i] == "Red":
        taller_fighter_wins += 1
    elif blue_height[i] > red_height[i] and red_or_blue[i] == "Blue":
        taller_fighter_wins += 1

taller_win_pct = decimal_to_percentage(float(taller_fighter_wins) / total_fights)

red_reach = data.R_Reach_cms
blue_reach = data.B_Reach_cms

longer_fighter_wins = 0

for i in range(0,total_fights):
    if red_reach[i] > blue_reach[i] and red_or_blue[i] == "Red":
        longer_fighter_wins += 1
    elif blue_reach[i] > red_reach[i] and red_or_blue[i] == "Blue":
        longer_fighter_wins += 1

longer_win_pct = decimal_to_percentage(float(longer_fighter_wins) / total_fights)

#Outut Below
print("\nUFC Data Analysis by Mike Fortin")
print("\nStatistics based on " + str(total_fights) + " fights between 1993 and 2019 ...")
print("\nThe red corner wins " + str(red_win_pct) + "% of the time.")
print("\nThe taller fighter wins " + str(taller_win_pct) + "% of the time. ")
print("\nThe fighter with the longer reach wins " + str(longer_win_pct) + "% of the time.")





