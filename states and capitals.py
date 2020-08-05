import csv
with open('states1.csv') as csv_file:
    readcsv = csv.reader(csv_file, delimiter = ',')
    for row in readcsv:
        print(row)