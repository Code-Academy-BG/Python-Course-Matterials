import csv
import os

from settings.testing import INPUT_DIR

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruits)

# In other words:
# for var in iterable:
#     do something


for fruit in fruits:
    if len(fruit) < 3:
        continue
    elif len(fruit) > 100000:
        continue
    else:
        print(fruit)
        # break This would cause an immediate exit from the loop


with open(os.path.join(INPUT_DIR, 'students_data.csv'), 'r') as source:
    reader = csv.reader(source)

    for row in reader:
        print(row)
