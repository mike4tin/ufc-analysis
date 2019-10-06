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
print("\nUFC Data Analysis by Mike Fortin")
print("\nThe red corner wins " + str(red_win_pct) + "% of the time.")





