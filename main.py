#Import the needed modules
import os
import csv


#Set Path
csvpath = os.path.join("Resources", "Office_clean.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip header
    header = next(csvreader)

    list_of_episodes = []


    for rows in csvreader:
        list_of_episodes.append(rows[1])
        print(list_of_episodes)

