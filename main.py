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
    top_five = []

    for rows in csvreader:   
        list_of_episodes.append(rows[1])
        if float(rows[3]) >= 8:
            top_five.append(rows[0,1,3,7,9])
            
        

print(top_five)
