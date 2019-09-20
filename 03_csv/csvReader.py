import csv
import random

occupations = {}
with open('occupations.csv', mode = 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        occupations[row["Job Class"]] = float(row["Percentage"])

job = random.randint(0, 997)  ##ignores last row because of 997



def randomJob():
    total = 0;
    for key in occupations:
        total += occupations[key]
        if (total * 10 >= job):
            return key

print(randomJob())
