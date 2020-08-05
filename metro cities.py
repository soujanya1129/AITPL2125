import csv
with open('cities longitude latitude1.csv') as csv_file:
    readcsv = csv.reader(csv_file, delimiter = ',')
    for row in readcsv:
        print(row)