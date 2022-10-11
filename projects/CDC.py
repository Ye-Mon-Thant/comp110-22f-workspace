import csv

with open ('projects\GHG.csv', mode = 'r') as file:
    csvFile = csv.reader(file)

    for lines in csvFile:
        print(lines, "\n")
    