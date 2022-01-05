# this assumes that gradebook-random is in the same folder as this starter file

import csv

with open('gradebook-random.csv',newline='') as gradefile:
    reader = csv.DictReader(gradefile, fieldnames=['id','hwk','exam','code','cs','att'])
    gradebook = [] # an empty list
    for row in reader:
        gradebook.append({'id': row['id'],
                          'hwk': row['hwk'],
                          'exams': row['exam'],
                          'coding': row['code'],
                          'conc': row['cs'],
                          'attended': row['att']})

prior_coding = list(filter(lambda row : row['coding'] == "x", gradebook))
no_prior_coding = list(filter(lambda row : row['coding'] != "x", gradebook))

def avg(rowlist, forcol):
    '''Compute average of given column in list of rows'''
    total = 0
    for row in rowlist:
        total = total + row[forcol]
    return total / len(rowlist)

# -------------------------------------------
# removing duplicates

def distinct(fromlist):
    unique = []
    for item in fromlist:
        if not(item in unique):
            unique.append(item)
    return unique

print(distinct([6, 2, 6, 4, 5, 5]))
