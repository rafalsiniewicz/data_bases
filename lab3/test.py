import csv
with open('AB_NYC_2019.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file)
    #for i, row in enumerate(csv_reader):
    #    if i > 0:
    for i, row in enumerate(csv_reader):
        print(i, row[0])