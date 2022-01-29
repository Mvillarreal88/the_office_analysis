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
    top_episodes = []


    for rows in csvreader:   
        list_of_episodes.append(rows[1])
        if float(rows[3]) >= 9:
                top_episodes.append(rows[1])            
        





#print data analysis 

print(["Episodes list"])
print(["------------------------"])
print(["Episodes: " + str(list_of_episodes)])