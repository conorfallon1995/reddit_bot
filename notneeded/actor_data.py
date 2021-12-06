import csv
from collections import Counter

list = []

with open('actor_queries.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        list.append(int(row[0]))

count_dict = sorted(Counter(list).items())

values_list = []

for row in count_dict:
    values_list.append(row[1])

print(values_list)

print(len(values_list))