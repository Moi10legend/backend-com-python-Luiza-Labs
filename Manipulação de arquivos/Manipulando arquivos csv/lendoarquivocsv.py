import csv

with open('example.csv', "r") as arquivo:
    reader = csv.reader(arquivo)
    for row in reader:
        print(row)